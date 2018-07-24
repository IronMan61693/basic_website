#!/usr/bin/env python3

from flask import Flask, render_template, redirect, flash, url_for
from dbconnect import connectMe
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def intro_page():
	return render_template("base.html", title='Wacky Fun')


@app.route('/home')
def home():
	return render_template("homePage.html", title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = LoginForm()

	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('intro_page'))

	return render_template("loginPage.html", title='Sign In', form=form)

# @app.route('/hidden')
# def hiddenPage():


if __name__ == "__main__":
	app.run(debug=True)
