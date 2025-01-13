from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.secret_key = 'quizziprocks'
#admin = Admin(app, name='Quiz Admin', template_mode='bootstrap3')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

migrate = Migrate(app, db)

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Field to indicate admin status

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    responses = db.relationship('Response', backref='quiz_attempt', lazy=True)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_attempt_id = db.Column(db.Integer, db.ForeignKey('quiz_attempt.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)  # Add this
    selected_option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)  # Add this
    correct = db.Column(db.Boolean, nullable=False)
    question = db.relationship('Question', backref='responses', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    options = db.relationship('Option', backref='question', lazy=True)
    # Remove the foreign key to Option here
    correct_option_id = db.Column(db.Integer, nullable=True)  # We'll update this after creating options

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)  # Add this to mark correct option
    
# Custom ModelView to restrict access
class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

# Custom AdminIndexView to restrict access to the admin dashboard
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        if not current_user.is_admin:
            return redirect(url_for('home'))
        return super(MyAdminIndexView, self).index()
 

# Initialize the admin with the custom index view
admin = Admin(app, index_view=MyAdminIndexView(), template_mode='bootstrap3')
admin.add_link(MenuLink(name='Back to Site', url='/'))

class QuizAttemptModelView(AdminModelView):
    column_list = ('id', 'user_id', 'timestamp', 'responses')
    column_formatters = {
        'user': lambda v, c, m, p: m.user.username,
        'responses': lambda v, c, m, p: len(m.responses)
    }

class ResponseModelView(AdminModelView):
    column_list = ('id', 'user_id', 'question', 'selected_option_id', 'correct')
    column_formatters = {
        'user': lambda v, c, m, p: m.user.username,
        'question': lambda v, c, m, p: m.question.text,
        'selected_option': lambda v, c, m, p: m.selected_option_id.text
    }

# Add views for User and Question models
admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Question, db.session))
admin.add_view(ResponseModelView(Response, db.session))
admin.add_view(AdminModelView(Option, db.session))
admin.add_view(QuizAttemptModelView(QuizAttempt, db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Quiz questions
quiz_data = [
    {"question": "What is the output of `print(2**3)`?", "options": ["6", "8", "9", "12"], "answer": "8"},
    {"question": "Which data type is mutable in Python?", "options": ["tuple", "string", "list", "int"], "answer": "list"},
    {"question": "What does `len()` do in Python?", "options": ["Finds length", "Sorts list", "Checks type", "Converts type"], "answer": "Finds length"},
    {"question": "Which keyword is used to create a function in Python?", "options": ["function", "define", "def", "lambda"], "answer": "def"},
    {"question": "What is the time complexity of accessing an element in a dictionary?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)"},
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
            return redirect(url_for('register'))

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('login'))
    
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for('home'))


# @app.route('/quiz')
# @login_required
# def quiz():
#     questions = Question.query.all()
#     return render_template('quiz.html', questions=questions)

@app.route('/quiz')
@login_required
def quiz():
    questions = Question.query.all()
    app.logger.debug(f"Found {len(questions)} questions")
    for q in questions:
        app.logger.debug(f"Question {q.id}: {q.text}")
        app.logger.debug(f"Options: {[o.text for o in q.options]}")
    return render_template('quiz.html', questions=questions)

# Add this debug route to check data
@app.route('/debug')
def debug():
    questions = Question.query.all()
    output = []
    for q in questions:
        q_dict = {
            'id': q.id,
            'text': q.text,
            'options': [{
                'id': opt.id,
                'text': opt.text,
                'is_correct': opt.is_correct
            } for opt in q.options]
        }
        output.append(q_dict)
    return jsonify(output)

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # Create new quiz attempt
    quiz_attempt = QuizAttempt(user_id=current_user.id)
    db.session.add(quiz_attempt)
    db.session.flush()  # Get ID before committing
    
    answers = request.form
    print("answers", answers)
    score = 0
    
    for question_id, selected_option_id in answers.items():
        if question_id.startswith('q_'):
            q_id = int(question_id.split('_')[1])
            opt_id = int(selected_option_id)
            
            # Get selected option
            selected_option = Option.query.get(opt_id)
            
            # Create response
            response = Response(
                user_id=current_user.id,
                quiz_attempt_id=quiz_attempt.id,
                question_id=q_id,
                selected_option_id=opt_id,
                correct=selected_option.is_correct
            )
            
            if selected_option.is_correct:
                score += 1
            
            print('resp', response)
            db.session.add(response)
    
    db.session.commit()
    flash(f'Quiz submitted! Score: {score}', 'success')
    return redirect(url_for('history'))

@app.route('/history')
@login_required
def history():
    # Retrieve all quiz attempts for the current user
    quiz_attempts = QuizAttempt.query.filter_by(user_id=current_user.id).order_by(QuizAttempt.timestamp.desc()).all()
    return render_template("history.html", quiz_attempts=quiz_attempts)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
