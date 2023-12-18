# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from .models_task_8 import LoginForm
from .forms_task_8 import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_2.db'
app.config['SECRET_KEY'] = '123qwerty'
db.init_app(app)
csrf = CSRFProtect(app)


def add_user(name, lastname, email, password):
    new_user = User(firstname=name, lastname=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()


def hash_password(user, password):
    return hash(password + user)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    form_errors = []
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        if User.query.filter(User.firstname == firstname, User.lastname == lastname).count() > 0:
            form_errors.append(f'Username already taken!')
        if User.query.filter(User.email == email).count() > 0:
            form_errors.append(f'Email {email} already taken!')
        else:
            print(f'Adding user {firstname}!')
            add_user(firstname, lastname, email, hash_password(firstname, form.password.data))
            form_notifications = [f'User {firstname} successfully registered!']
            return render_template(
                'form_task_4.html', form=form, form_notifications=form_notifications)

    return render_template('form_task_4.html', form=form, form_errors=form_errors)


@app.cli.command('init-db')
def initdb():
    db.create_all()
    print('Database created successfully!')
