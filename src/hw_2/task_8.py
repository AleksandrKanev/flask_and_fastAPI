# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)

app.secret_key = b'3f487e7ce298b5aad0b53b115eb245721cc25558d1af8b56d5646a991f4b5e75'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        flash(f"Привет, {name}!", 'success')
        return redirect(url_for('index'))

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
