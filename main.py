from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, мир! Эта страница - начало моего проекта Link Statistic. dev: @Fedos-py'


@app.route('/about')
def about():
    return '<center>Link Statistic - проект, в котором будут реализован функционал для укорочения ссылок' \
           ' и мониторинга статистики перехода по ним.<br><a href="https://t.me/fedospy">' \
           'Связь с разработчиком</a></center>'


if __name__ == "__main__":
    app.run()
