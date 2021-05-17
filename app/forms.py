from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    register = SubmitField('Register')


class TaskForm(FlaskForm):
    item = StringField('item', validators=[DataRequired()])
    add = SubmitField('Add Task')


class ListForm(FlaskForm):
    list = StringField('Task Name', validators=[DataRequired()])
    add = SubmitField('Add Task')
    category = StringField('Category')


class TaskEditForm(FlaskForm):
    item = StringField('item', validators=[DataRequired()])
    rename = SubmitField('Rename Task')
    changeCategory = StringField('Change Category')
