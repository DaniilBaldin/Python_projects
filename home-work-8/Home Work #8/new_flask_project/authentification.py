import hashlib
import os

from flask import Blueprint, request, render_template, session, g, url_for
from werkzeug.utils import redirect
from sqlalchemy.exc import MultipleResultsFound, NoResultFound, IntegrityError

from database import db
from model import UserModel

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        try:
            user_login = request.form['login']
            user_name = request.form['name']
            user_password = request.form['password']
            user_salt = os.urandom(32)
            user_hex = hashlib.pbkdf2_hmac('sha512', bytes(user_password, 'utf-8'), user_salt, 120000)
            user = UserModel(username=user_login, name=user_name, password=user_hex, salt=user_salt)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return render_template('reg.html', title_name='Registration', message='Already registered?')

        return redirect(url_for('auth.root'))
    return render_template('reg.html', title_name='Registration', message='Already registered?')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        user_password = request.form['password']
        user_salt = os.urandom(32)
        try:
            g.user = db.session.query(UserModel.user_name.label('login'),
                                      UserModel.name).filter(
                UserModel.username == user_name
            ).filter(
                UserModel.password == user_password
            ).one()
            '''
             select user.user_name as login, user.name from user where user.user_name = ? and user.password = ?
             '''
        except MultipleResultsFound:
            return render_template('login.html', message='There is more than one user with this name')
        except NoResultFound:
            return render_template('login.html', message='No such user/password in database')
        user_hex = hashlib.pbkdf2_hmac('sha512', bytes(str(user_password), 'utf-8'), user_salt, 120000)
        if user_hex == user_password:
            session.clear()
            session['user'] = {'user_name': g.user.login, 'name': g.user.name}
    g.user = session.get('user')
    if g.user is not None:
        return redirect(url_for('auth.root'))
    return render_template('login.html')


@auth.route('/')
def root():
    g.user = session.get('user')
    if g.user is not None:
        return render_template('root.html', login=g.user['user_name'], name=g.user['name'])
    return render_template('root.html')


@auth.route('/logout')
def logout():
    g.user = session.get('user')
    if g.user is not None:
        session.clear()
        return redirect(url_for('auth.root'))
    return redirect(url_for('auth.login'))


@auth.errorhandler(400)
def internal_serv_error(e):
    return render_template('errors/400.html', e=e), 400


@auth.errorhandler(500)
def internal_serv_error(e):
    return render_template('errors/500.html', e=e), 500
