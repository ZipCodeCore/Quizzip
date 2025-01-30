import datetime
from flask import jsonify, render_template, request, redirect, url_for, flash
from flask import session
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
            return redirect(url_for('app.home'))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for('app.login'))

    return render_template('login.html')

@app_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for('app.home'))

from random import sample
from sqlalchemy import not_, exists

# Add this new route in routes.py
@app_bp.route('/select-topic', methods=['GET', 'POST'])
@login_required
def select_topic():
    # Get unique topics from questions
    topics = db.session.query(Question.tech).distinct().all()
    print("topics:", topics)
    topics = [topic[0] for topic in topics]  # Convert from tuples to list

    if request.method == 'POST':

        selected_topic = request.form.get('topic')
        quiz_attempt = QuizAttempt(user_id=current_user.id)
        quiz_attempt.starttimestamp = datetime.datetime.now()
        quiz_attempt.tech = selected_topic
        db.session.add(quiz_attempt)

        db.session.commit()
        db.session.flush()
        session['quiz_attempt_id'] = quiz_attempt.id
        print("QID ",quiz_attempt.id)

        return redirect(url_for('app.quiz', topic=selected_topic))

    return render_template('select_topic.html', topics=topics)

# this has a subtle bug: the last page on answers wasn't being saved
# so I hacked the paging so that it goes one page beyond the last page
# and then redirects to the history page after submitting
@app_bp.route('/quiz')
@login_required
def quiz():
    QUESTIONS_PER_PAGE = 4
    page = request.args.get('page', 1, type=int)
    selected_topic = request.args.get('topic')

    # Initialize or get quiz questions from session
    if 'quiz_questions' not in session or request.args.get('new_quiz'):
        # Your existing question selection logic here
        base_query = Question.query
        if selected_topic:
            base_query = base_query.filter(Question.tech == selected_topic)

        unsolved_questions = base_query.filter(
            not_(exists().where(
                (Response.question_id == Question.id) &
                (Response.user_id == current_user.id) &
                (Response.correct == True)
            ))
        ).all()

        if len(unsolved_questions) < 12:  # Need 12 questions total
            solved_questions = base_query.filter(
                Question.id.notin_([q.id for q in unsolved_questions])
            ).all()

            remaining_needed = 12 - len(unsolved_questions)
            if solved_questions:
                random_solved = sample(solved_questions, min(remaining_needed, len(solved_questions)))
                questions = unsolved_questions + random_solved
            else:
                questions = unsolved_questions
        else:
            questions = sample(unsolved_questions, 12)

        # Store question IDs in session
        session['quiz_questions'] = [q.id for q in questions]
        session['quiz_answers'] = {}  # Initialize empty answers dict

    # Get questions for current page
    question_ids = session['quiz_questions']
    start_idx = (page - 1) * QUESTIONS_PER_PAGE
    end_idx = start_idx + QUESTIONS_PER_PAGE
    current_question_ids = question_ids[start_idx:end_idx]

    questions = Question.query.filter(Question.id.in_(current_question_ids)).all()
    total_pages = (len(question_ids) + QUESTIONS_PER_PAGE - 1) // QUESTIONS_PER_PAGE

    return render_template('quiz.html',
                         questions=questions,
                         selected_topic=selected_topic,
                         current_page=page,
                         total_pages=total_pages,
                         saved_answers=session.get('quiz_answers', {}))

import logging

@app_bp.route('/save-answers', methods=['POST'])
@login_required
def save_answers():
    # Save answers to session
    answers = request.form
    current_answers = session.get('quiz_answers', {})

    for key, value in answers.items():
        if key.startswith('q_'):
            current_answers[key] = value

    session['quiz_answers'] = current_answers

    # Log the current session data
    logging.debug(f"Current quiz answers: {session['quiz_answers']}")

    # Determine where to go next
    next_page = request.form.get('next_page', type=int)
    if next_page:
        return redirect(url_for('app.quiz', page=next_page))
    return redirect(url_for('app.quiz', page=1))

@app_bp.route('/submit', methods=['POST'])
@login_required
def submit():
    if 'quiz_questions' not in session:
        flash('No quiz in progress', 'error')
        return redirect(url_for('app.select_topic'))

    # Create new quiz attempt
    # get quiz attempt 
    qid = session['quiz_attempt_id']
    print("QID ",qid)
    quiz_attempt = QuizAttempt.query.get(int(qid))
    quiz_attempt.endtimestamp = datetime.datetime.now()
    db.session.add(quiz_attempt)
    db.session.flush()

    answers = session.get('quiz_answers', {})
    print("answers #", len(answers))
    score = 0

    for question_key, selected_option_id in answers.items():
        if question_key.startswith('q_'):
            q_id = int(question_key.split('_')[1])
            opt_id = int(selected_option_id)

            selected_option = Option.query.get(opt_id)

            response = Response(
                user_id=current_user.id,
                quiz_attempt_id=quiz_attempt.id,
                question_id=q_id,
                selected_option_id=opt_id,
                correct=selected_option.is_correct
            )

            if selected_option.is_correct:
                score += 1

            db.session.add(response)

    db.session.commit()

    # Clear quiz session data
    session.pop('quiz_questions', None)
    session.pop('quiz_answers', None)

    flash(f'Quiz submitted! Score: {score}', 'success')
    return redirect(url_for('app.history'))

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



@app_bp.route('/history')
@login_required
def history():
    # Retrieve all quiz attempts for the current user
    quiz_attempts = QuizAttempt.query.filter_by(user_id=current_user.id).order_by(QuizAttempt.endtimestamp.desc()).all()
    return render_template("history.html", quiz_attempts=quiz_attempts)
