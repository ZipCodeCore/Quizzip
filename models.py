import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from extensions import db

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def get_quiz_count(self):
        return QuizAttempt.query.filter_by(user_id=self.id).count()
    
    def get_correct_percentage(self):
        total_responses = Response.query.filter_by(user_id=self.id).count()
        if total_responses == 0:
            return 0
        correct_responses = Response.query.filter_by(user_id=self.id, correct=True).count()
        return round((correct_responses / total_responses) * 100, 1)
    
    def get_total_answered(self):
        return Response.query.filter_by(user_id=self.id).count()
    
    @staticmethod
    def get_total_questions():
        return Question.query.count()
        
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tech = db.Column(db.String(32), nullable=True)
    text = db.Column(db.String(500), nullable=False)
    options = db.relationship('Option', backref='question', lazy = "dynamic")
    correct_option_id = db.Column(db.Integer, nullable=True)

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"), nullable=False)
    #question = db.relationship("Question", backref="options")
    is_correct = db.Column(db.Boolean, default=False)

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tech = db.Column(db.String(32), nullable=True)
    starttimestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    endtimestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    responses = db.relationship('Response', backref='quiz_attempt', lazy = "dynamic")

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_attempt_id = db.Column(db.Integer, db.ForeignKey('quiz_attempt.id', ondelete="CASCADE"), nullable=False)
    #quiz_attempt = db.relationship('QuizAttempt', backref='responses')
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question = db.relationship('Question', backref='responses')
    selected_option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
