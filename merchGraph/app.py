# from flask import Flask, render_template,request
# from flask_mysqldb import MySQL
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return ('index.html')
#
#
#
# if __name__=='__main__':
#     app.run(debug = True)

from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chart")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
    app.run(debug=True)
