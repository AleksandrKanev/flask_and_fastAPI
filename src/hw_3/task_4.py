# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, render_template, request
from flask_wtf import CSRFProtect

from .models_task_4 import LoginForm
from .forms_task_4 import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '123qwerty'
db.init_app(app)
csrf = CSRFProtect(app)


def add_user(name, email, password):
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    form_errors = []
    if request.method == 'POST' and form.validate():
        username = form.name.data
        email = form.email.data
        if User.query.filter(User.name == username).count() > 0:
            form_errors.append(f'Username {username} already taken!')
        if User.query.filter(User.email == email).count() > 0:
            form_errors.append(f'Email {email} already taken!')
        else:
            print(f'Adding user {username}!')
            add_user(username, form.email.data, form.password.data)
            form_notifications = [f'User {username} successfully registered!']
            return render_template(
                'form_task_4.html', form=form, form_notifications=form_notifications)

    return render_template('form_task_4.html', form=form, form_errors=form_errors)


@app.cli.command('init-db')
def initdb():
    db.create_all()
    print('Database created successfully!')


if __name__ == '__main__':
    app.run(debug=True)
