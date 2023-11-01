from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, мир! Эта страница - начало моего проекта Link Statistic. dev: @Fedos-py'


if __name__ == "__main__":
    app.run()