from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, ValidationError, Email, EqualTo
from dbconnect import User


class LoginForm(Form):
	username = TextField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class RegistrationForm(Form):
	username = TextField('Username', validators=[Required()])
	email = TextField('Email', validators=[Required(), Email()])
	password = PasswordField('Password', validators=[Required()])
	password2 = PasswordField(
			'Repeat Password', validators=[Required(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('That username is taken.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('That email is already in use.')


