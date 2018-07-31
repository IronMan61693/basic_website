from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from run import *
from forms import LoginForm, RegistrationForm
from dbconnect import User



@app.route('/')
@app.route('/index')
def intro_page():
	return render_template("base.html", title='Wacky Fun')


@app.route('/home')
def home():
	return render_template("homePage.html", title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	if current_user.is_authenticated:
		return redirect(url_for('intro_page'))

	form = LoginForm()

	if form.validate_on_submit():

		user = User.query.filter_by(username=form.username.data).first()

		if user is None or not user.check_password(form.password.data):

			flash('Invalid username or password')
			return redirect(url_for('login_page'))

		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('intro_page'))

	return render_template("loginPage.html", title='Sign In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('intro_page'))

@app.route('/route', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('intro_page'))

	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Yay, you are now a registered member')
		return redirect(url_for('login_page'))

	return render_template('register.html', title = 'Register', form=form)

@app.route('/hidden')
def hidden_page():
	return render_template("hiddenPage.html", title='Sneaky Page')

