from flask import Flask
#from flask_migrate import Migrate
import datetime
from extensions import db, login_manager
from routes import app_bp
from admin import OptionViewWithInlineModel
from flask_admin import Admin
#migrate = Migrate(app, db)
from admin import MyAdminIndexView, MyAdminModelView, QuizAttemptModelView, ResponseModelView, RespViewWithInlineModel
from flask_admin import Admin
from flask_admin.menu import MenuLink
#from flask_admin.contrib.sqla import ModelView
#from flask_admin.form import rules
#from flask_admin.model.form import InlineFormAdmin
#from flask_login import current_user, login_required
from extensions import db
from models import User, Question, Option, QuizAttempt, Response

def create_app(config_object='settings'):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    #app = Flask(__name__)
    app.secret_key = 'quizziprocks'

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config['SQLALCHEMY_ECHO'] = True


    admin_bp = Admin(app, index_view=MyAdminIndexView(), template_mode='bootstrap3')
    admin_bp.add_link(MenuLink(name='Back to Site', url='/'))

    # Update admin views
    # Add views for User and Question models
    admin_bp.add_view(MyAdminModelView(User, db.session))
    admin_bp.add_view(ResponseModelView(Response, db.session))
    #admin_bp.add_view(ModelView(Response, db.session))
    #admin_bp.add_view(QuizAttemptModelView(QuizAttempt, db.session))
    admin_bp.add_view(RespViewWithInlineModel(QuizAttempt, db.session))

    admin_bp.add_view(OptionViewWithInlineModel(Question, db.session))

    register_extensions(app)
    app.register_blueprint(app_bp)
    return app

def register_extensions(app):
    db.init_app(app)

# Quiz questions
quiz_data = [
    {"question": "What is the output of `print(2**3)`?", "options": ["6", "8", "9", "12"], "answer": "8"},
    {"question": "Which data type is mutable in Python?", "options": ["tuple", "string", "list", "int"], "answer": "list"},
    {"question": "What does `len()` do in Python?", "options": ["Finds length", "Sorts list", "Checks type", "Converts type"], "answer": "Finds length"},
    {"question": "Which keyword is used to create a function in Python?", "options": ["function", "define", "def", "lambda"], "answer": "def"},
    {"question": "What is the time complexity of accessing an element in a dictionary?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)"},
]

if __name__ == '__main__':
    app = create_app()
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
