from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

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
            return redirect(url_for('quiz'))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for('login'))

@app.route('/quiz')
@login_required
def quiz():
    return render_template("quiz.html", questions=quiz_data)

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    user_answers = request.form
    score = 0

    for i, question in enumerate(quiz_data):
        if user_answers.get(f"q{i}") == question["answer"]:
            score += 1

    return render_template("result.html", score=score, total=len(quiz_data))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    