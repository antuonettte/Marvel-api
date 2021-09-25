from app.blueprints.auth.models import User
from .import bp as app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app import db

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for the user in our database
        user = User.query.filter_by(email=email).first()
        # if the email and/or password don't match,
        if user is None or not user.check_password(password):
            # show an error messages
            flash('You typed in either an incorrect email or password', 'danger')
            # redirect to the login page
            return redirect(url_for('auth.login'))
        # otherwise
        # log the user in
        login_user(user)
        flash('You have logged in successfully!', 'info')
        return redirect(url_for('main.home'))
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        user = User.query.filter_by(email=request.form.get('email')).first()

        if user is not None:#Checks if the email is already in use
            flash('That useralready exists. Please try another email addres', 'warning')
            return redirect(url_for('auth.register'))

        #Checks if password and confirm password match
        if request.form.get('pasword') != request.form.get('confirm_pasword'):
            flash('Your passwords do not match.','danger')
            return redirect(url_for('auth.register'))

        u=User()
        u.from_dict(request.form)
        u.save()

        flash('User has registered successfully', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('main.home'))
