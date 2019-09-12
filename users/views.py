from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from .forms import LoginForm, RegistrationForm
from .models import User

users_app = Blueprint('users_app', __name__)


@users_app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            user = User.query.filter_by(email=login_form.email.data).first()
            if user:
                if user.check_password(login_form.password.data):
                    login_user(user)
                    return redirect(url_for('users_app.profile', id=user.id))
            else:
                flash('wrong user name or password please try again', 'danger')
                # return redirect(url_for('users_app.login'))


    return render_template('users/login.html', login_form=login_form)


@users_app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if request.method == 'POST':
        if register_form.validate_on_submit():
            user = User()
            register_form.populate_obj(user)
            user.set_password(register_form.password.data)
            user.save()
            flash('account created successfully you can login now', 'success')
            return redirect(url_for('users_app.login'))


    return render_template('users/register.html', register_form=register_form)




@users_app.route('/login_success')
@login_required
def login_success():
    return render_template('users/login_success.html')


@users_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users_app.login'))


@users_app.route('/profile/<int:id>')
def profile(id):
    user = User.query.get_or_404(id)
    return render_template('users/profile.html', user=user)
