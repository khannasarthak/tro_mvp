from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template, request
from datetime import datetime,timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/tromvp'
db = SQLAlchemy(app)


class mvp(db.Model):
	__tablename__ = 'mvp'
	name = db.Column('name',db.Unicode, primary_key=True)
	lowertime = db.Column('lowertime', db.Integer)
	uppertime = db.Column('uppertime', db.Integer)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mvpdb",methods = ['POST', 'GET'])
def mvpdb():	
	return render_template('mvpdb.html')

@app.route("/mvpcheck",methods = ['POST', 'GET'])
def mvpcheck():	
	formname = request.form['mvpname']
	now = datetime.now()
	dietime = now.strftime("%H:%M")
	mvpdetails = mvp.query.filter(mvp.name==formname)
	# print ('/////',mvpdetails)
	for details in mvpdetails:
		lowtime = details.lowertime
		uptime = details.uppertime
	# print ("-------",lowtime,'==============',uptime)
	reslow =  (now + timedelta(minutes=int(lowtime))).strftime("%H:%M")
	resup  =  (now + timedelta(minutes=int(uptime))).strftime("%H:%M")
	print ('++++', reslow,'+++',resup)

	return render_template('mvpdb.html', mvpdetails = mvpdetails, dietime = dietime, reslow = reslow, resup= resup)


@app.route("/chart")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
    app.run(debug=True)
