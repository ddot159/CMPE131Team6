
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
<<<<<<< HEAD
    submit = SubmitField('Sign In')
=======
    submit = SubmitField('Sign In')
>>>>>>> 8659953c2a68d8f3cad914c066cb71730d6bcc99
