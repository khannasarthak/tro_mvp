from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template, request
from datetime import datetime,timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/tromvp'
db = SQLAlchemy(app)


class mvp(db.Model):	# mvp database
	__tablename__ = 'mvp'
	name = db.Column('name',db.Unicode, primary_key=True)
	lowertime = db.Column('lowertime', db.Integer)
	uppertime = db.Column('uppertime', db.Integer)

class deadmvp(db.Model):   #dead mvp table
	__tablename__ = 'deadmvp'
	name = db.Column('name',db.Unicode, primary_key=True)
	deathtime = db.Column('deathtime', db.Time)

	def __init__(self,name, deathtime):	# needed to insert/update
		self.name = name
		self.deathtime = deathtime
	


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mvpdb",methods = ['POST', 'GET'])
def mvpdb():	
	test = deadmvp('Eddga (pay_fild11)','04:06')
	print ('++++++++++', test)
	db.session.add(test)
	db.session.commit()
	return render_template('mvpdb.html')

@app.route("/mvpcheck",methods = ['POST', 'GET'])
def mvpcheck():	
	formname = request.form['mvpname']
	now = datetime.now()
	dietime = now.strftime("%H:%M")
	mvpdetails = mvp.query.filter(mvp.name==formname)
	
	for details in mvpdetails:
		lowtime = details.lowertime
		uptime = details.uppertime
	# print ("-------",lowtime,'==============',uptime)
	reslow =  (now + timedelta(minutes=int(lowtime))).strftime("%H:%M")
	resup  =  (now + timedelta(minutes=int(uptime))).strftime("%H:%M")
	# print ('++++', reslow,'+++',resup)

	test = deadmvp(formname,dietime)
	print ('++++++++++', test)
	db.session.add(test)
	db.session.commit()

	return render_template('mvpdb.html', mvpdetails = mvpdetails, dietime = dietime, reslow = reslow, resup= resup)


@app.route("/chart")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
    app.run(debug=True)
