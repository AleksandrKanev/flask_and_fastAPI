# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        if int(request.form.get('age')) > 18:
            return render_template('index.html', username=name)
        else:
            return render_template('error_age.html', username=name)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
