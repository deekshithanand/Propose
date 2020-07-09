from flask import Blueprint, request, render_template, redirect, url_for, flash
from .forms import *
from src.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
from sqlalchemy import exc

#blueprint here
auth_bp = Blueprint('auth', __name__, template_folder='templates')

#routes
@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():

    if request.method == 'GET':
        form = SignUpForm()
        return render_template('signup.html', form=form)

    if request.method == 'POST':
        form = SignUpForm(request.form)
        if form.validate():
            # check if user exist and add user

            existing_user = User.query.filter(
                User.username == form.uname.data or User.email == form.email.data).all()
            if existing_user:
                flash("Username or Email Already Existing", 'danger')
                return redirect(url_for('auth.signup'))
            else:
                # add user
                new_user = User(
                    username=form.uname.data,
                    email=form.email.data,
                    password=generate_password_hash(form.pwd.data)
                )
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    flash("User Signed Up",'success')
                    return redirect(url_for('auth.login'))
                except exc.IntegrityError:
                    db.session.rollback()
                    return 500
                
        else:
            # form invalidation
            flash("Form with invalid Data",category ='warning')
            return render_template('signup.html',form=form)

@auth_bp.route('/logout')
def logout():
    pass


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        formData = LoginForm()
        return render_template('login.html',form=formData)

    if request.method == 'POST':
        formData = LoginForm(request.form)
        uname = formData.uname.data
        pwd = formData.pwd.data
        user = User.query.filter(User.username == uname).first()
        if user:
            print(user)
            if check_password_hash(user.password,pwd):
                return user.username
            else: 
                return 'Login Failed'

