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
	dead = db.Column('dead', db.Integer)
	deathtime = db.Column('deathtime', db.Time)
	reslow = db.Column('reslow', db.Time)
	resup = db.Column('resup', db.Time)
	date = db.Column('date', db.Date)


	def __init__(self,name, deathtime, dead, reslow, resup, date):	# needed to insert/update
		self.name = name
		self.deathtime = deathtime
		self.dead = dead
		self.reslow = reslow
		self.resup = resup
		self.date = date

class users(db.Model):   #dead mvp table
	__tablename__ = 'users'
	name = db.Column('username',db.Unicode, primary_key=True)

	def __init__(self,username):	# needed to insert/update
		self.username = username
		
	


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mvpdb",methods = ['POST', 'GET'])
def mvpdb():	

	mvpdetails = mvp.query.filter(mvp.dead==1).order_by(mvp.date.asc()).order_by(mvp.reslow.asc())
	return render_template('mvpdb.html', mvpdetails = mvpdetails)

@app.route("/mvpcheck",methods = ['POST', 'GET'])
def mvpcheck():	
	formname = request.form['mvpname']
	mvpname = mvp.query.filter(mvp.name==formname).first()
	now = datetime.now()
	dietime = now.strftime("%H:%M")

	 
	mvpdetails1 = mvp.query.filter(mvp.name==formname)
	if mvpname is not None:		#Update if exists
		# print ('EXSITS')
		for details in mvpdetails1:
			lowtime = details.lowertime
			uptime = details.uppertime
		reslow =  (now + timedelta(minutes=int(lowtime))).strftime("%H:%M")
		resup  =  (now + timedelta(minutes=int(uptime))).strftime("%H:%M")
		diedate = (now + timedelta(minutes=int(uptime))).strftime("%Y-%m-%d") #
	
		update_this = mvp.query.filter_by(name = formname).first()		
		# print (update_this)
		update_this.deathtime = dietime
		update_this.dead = 1
		update_this.resup = resup
		update_this.reslow = reslow
		update_this.date = diedate
		db.session.commit()

	mvpdetails = mvp.query.filter(mvp.dead==1).order_by(mvp.date.asc()).order_by(mvp.reslow.asc())
	return render_template('mvpdb.html', mvpdetails = mvpdetails)


@app.route("/login")
def login():    
    return render_template('login.html')





@app.route("/chart")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)




if __name__ == "__main__":
    app.run(debug=True)
