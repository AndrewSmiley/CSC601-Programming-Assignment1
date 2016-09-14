from flask import Flask, render_template,request
import json
from logic import calculate_interest
from model import *
app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('index.html', my_data="Hello, world!")

@app.route("/test")
def test():
    print request.args.get("amount")
    print request.args.get("years")
    print request.args.get("interest")
    value = calculate_interest(float(request.args.get("amount")),float(request.args.get("years")),float(request.args.get("interest")))
    IOWriter.save_row(Row(request.args.get("amount"), request.args.get("years"), request.args.get("interest"),unicode(value)))
    return json.dumps({"value": value})
if __name__ == '__main__':
    app.run()
