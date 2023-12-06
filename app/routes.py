from flask import Flask, render_template, url_for, redirect, flash
from app.forms import RegistrationForm, LoginForm
from app.models import User, Book
from app import app, db, bcrypt

@app.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_paasword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_paasword)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created! You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You have been logged in!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')