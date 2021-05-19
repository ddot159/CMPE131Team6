from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    register = SubmitField('Sign Up')


class TaskForm(FlaskForm):
    item = StringField('item', validators=[DataRequired()])
    filter = SubmitField('Filter')


class ListForm(FlaskForm):
    list = StringField('Task Name', validators=[DataRequired()])
    add = SubmitField('Add Task')
    category = StringField('Category')
    priority = BooleanField('Priority')
    end = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])


class EditForm(FlaskForm):
    rename = StringField('New Task')
    changeCategory = StringField('New Category')
    newDate = DateField('New Deadline (Required)', format='%Y-%m-%d')
    edit = SubmitField('Confirm Edit')
