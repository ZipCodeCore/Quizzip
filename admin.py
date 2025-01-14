
from flask import redirect, url_for, request
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
#from flask_admin.form import rules
from flask_admin.model.form import InlineFormAdmin
from flask_login import current_user, login_required
from models import User, Question, Option, QuizAttempt, Response

# Custom ModelView to restrict access
class MyAdminModelView(ModelView):
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
            return redirect(url_for('app.home'))
        return super(MyAdminIndexView, self).index()
 
#
# Initialize the admin with the custom index view
#

class QuizAttemptModelView(MyAdminModelView):
    column_list = ('id', 'user_id', 'starttimestamp', 'endtimestamp', 'responses')
    column_formatters = {
        'user': lambda v, c, m, p: m.user.username,
        #'responses': lambda v, c, m, p: len(m.responses)
    }

class ResponseModelView(MyAdminModelView):
    column_list = ('id', 'user_id', 'question', 'selected_option_id', 'is_correct')
    column_formatters = {
    #     'user': lambda v, c, m, p: m.user.username,
        'question': lambda v, c, m, p: m.question.text,
    #     'selected_option': lambda v, c, m, p: m.selected_option_id.text
    }

class OptionViewWithInlineModel(MyAdminModelView):
    inline_models = [(Option, dict(form_columns=['id', 'text', 'is_correct']))]

class RespViewWithInlineModel(MyAdminModelView):
    inline_models = [(Response, dict(form_columns=['id', 'selected_option_id', 'correct']))]
