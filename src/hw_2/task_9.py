# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


from flask import Flask, request, redirect, render_template, url_for, make_response, session

app = Flask(__name__)
app.secret_key = b'3f487e7ce298b5aad0b53b115eb245721cc25558d1af8b56d5646a991f4b5e75'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("username")
        mail_ = request.form.get("email")
        session[name] = mail_
        return redirect(url_for('login', name=name))
    return render_template('form_name_and_email.html')


@app.route('/login/<name>', methods=['GET', 'POST'])
def login(name):
    if request.method == 'POST':
        session.pop(name)
        return redirect(url_for('index'))
    return render_template('login.html', username=name)


if __name__ == '__main__':
    app.run(debug=True)
