import datetime
from flask import jsonify, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from extensions import db, bcrypt, login_manager

from models import User, Question, Option, QuizAttempt, Response

from flask import Blueprint

app_bp = Blueprint('app', __name__)


@login_manager.user_loader
def load_user(user_id):
    # Load the user from your database or other storage mechanism
    # For example, if you are using SQLAlchemy:
    return User.query.get(int(user_id))


@app_bp.route('/')
def home():
    stats = {
        'quiz_count': 0,
        'correct_percentage': 0,
        'total_answered': 0,
        'total_questions': User.get_total_questions()
    }
    
    if current_user.is_authenticated:
        stats.update({
            'quiz_count': current_user.get_quiz_count(),
            'correct_percentage': current_user.get_correct_percentage(),
            'total_answered': current_user.get_total_answered()
        })
    return render_template("home.html", **stats)

@app_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
            return redirect(url_for('app.register'))

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('app.login'))
    
    return render_template("register.html")

@app_bp.route('/login', methods=['GET', 'POST'])
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

@app_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for('app.home'))


# @app_bp.route('/quiz')
# @login_required
# def quiz():
#     questions = Question.query.all()
#     print(f"Found {len(questions)} questions")
#     for q in questions:
#         print(f"Question {q.id}: {q.text}")
#         print(f"Options: {[o.text for o in q.options]}")
#     return render_template('quiz.html', questions=questions)

from random import sample
from sqlalchemy import not_, exists

@app_bp.route('/quiz')
@login_required
def quiz():
    # Number of questions per quiz
    QUIZ_SIZE = 5

    # Get questions user hasn't answered correctly
    unsolved_questions = Question.query.filter(
        not_(exists().where(
            (Response.question_id == Question.id) &
            (Response.user_id == current_user.id) &
            (Response.correct == True)
        ))
    ).all()

    # If we don't have enough unsolved questions, get some random ones
    if len(unsolved_questions) < QUIZ_SIZE:
        # Get remaining needed questions
        solved_questions = Question.query.filter(
            Question.id.notin_([q.id for q in unsolved_questions])
        ).all()
        
        remaining_needed = QUIZ_SIZE - len(unsolved_questions)
        if solved_questions:
            random_solved = sample(solved_questions, min(remaining_needed, len(solved_questions)))
            questions = unsolved_questions + random_solved
        else:
            questions = unsolved_questions
    else:
        # Random sample from unsolved questions
        questions = sample(unsolved_questions, QUIZ_SIZE)

    return render_template('quiz.html', questions=questions)

# Add this debug route to check data
@app_bp.route('/debug')
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

@app_bp.route('/submit', methods=['POST'])
@login_required
def submit():
    # Create new quiz attempt
    quiz_attempt = QuizAttempt(user_id=current_user.id)
    quiz_attempt.starttimestamp = datetime.datetime.now()
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
    return redirect(url_for('app.history'))

@app_bp.route('/history')
@login_required
def history():
    # Retrieve all quiz attempts for the current user
    quiz_attempts = QuizAttempt.query.filter_by(user_id=current_user.id).order_by(QuizAttempt.endtimestamp.desc()).all()
    return render_template("history.html", quiz_attempts=quiz_attempts)

