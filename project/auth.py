from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from .models import User
from .forms import RegistrationForm, LoginForm
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        user = User.query.filter_by(email=email).first()
        print(f"Trying to log in with email: {email}")
        print(f"User found: {user}")

        if not user:
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

    return render_template('login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        new_user = User(email=email, name=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!')

        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
