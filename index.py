from flask import Flask, render_template, flash, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/out')
def out():
    return render_template('out.html', title='Выход')


@app.route('/country')
def country():
    return render_template('country.html', title='Страны')


@app.route('/russia')
def russia():
    return render_template("russia.html", title='Города России')


@app.route('/brazil')
def brazil():
    return render_template("brazil.html", title='Города Бразилии')


@app.route('/usa')
def usa():
    return render_template("usa.html", title='Города США')


@app.route('/italy')
def italy():
    return render_template("italy.html", title='Города Италии')


@app.route('/moscow')
def moscow():
    return render_template("moscow.html", title='Достопримечательности Москвы')


@app.route('/pyter')
def pyter():
    return render_template("pyter.html", title='Достопримечательности Санкт-Перербурга')


@app.route('/altay')
def altay():
    return render_template("altay.html", title='Природа Алтая')


@app.route('/kazan')
def kazan():
    return render_template("kazan.html", title='Достопримечательности Казани')


@app.route('/rio')
def rio():
    return render_template("rio.html", title='Достопримечательности Рио-де-Жанейро')


@app.route('/brazilia')
def brazilia():
    return render_template("brazilia.html", title='Достопримечательности Бразилии')


@app.route('/salvador')
def salvador():
    return render_template("salvador.html", title='Достопримечательности Сальвадора')


@app.route('/newyork')
def newyork():
    return render_template("newyork.html", title='Достопримечательности Нью-Йорка')


@app.route('/sanfran')
def sanfran():
    return render_template("sanfran.html", title='Достопримечательности Сан-Франциско')


@app.route('/kolumbia')
def kolumbia():
    return render_template("kolumbia.html", title='Достопримечательности Колумбии')


@app.route('/losangeles')
def losangeles():
    return render_template("losangeles.html", title='Достопримечательности Лос-Анджелеса')


@app.route('/rim')
def rim():
    return render_template("rim.html", title='Достопримечательности Рима')


@app.route('/venice')
def venice():
    return render_template("venice.html", title='Достопримечательности Венеции')


@app.route('/milan')
def milan():
    return render_template("milan.html", title='Достопримечательности Милана')


@app.route('/piza')
def piza():
    return render_template("piza.html", title='Достопримечательности Пизы')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
