from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password_confirmation = PasswordField('password confirmation', validators=[DataRequired()])

    def validate(self):
        check_validate = super(RegistrationForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False

        if self.password.data != self.password_confirmation.data:
            self.password.errors.append('passwords dont match')
            self.password_confirmation.errors.append('passwords dont match')
            return False
        return True




class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
