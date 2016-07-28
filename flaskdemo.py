from flask import Flask, render_template
from database import db_session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/test")
def test():
    return render_template('test.html', my_data="Hello, world!")

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
