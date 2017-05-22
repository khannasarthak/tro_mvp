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
	return render_template('mvpdb.html')

@app.route("/mvpcheck",methods = ['POST', 'GET'])
def mvpcheck():	
	formname = request.form['mvpname']
	mvpname = deadmvp.query.filter(deadmvp.name==formname).first()
	now = datetime.now()
	dietime = now.strftime("%H:%M")
	if mvpname is not None:		#Update if exists
		# print ('EXSITS')
		update_this = deadmvp.query.filter_by(name = formname).first()		
		# print (update_this)
		update_this.deathtime = dietime
		# print ('AFTER UPDATE',update_this)
		db.session.commit()
	else:	# Insert if doesnt exist
		# print ('DOESNT EXSITS')
		row = deadmvp(formname,dietime)
		db.session.add(row) 	# to update
		db.session.commit()
		 
		

	
	mvpdetails = mvp.query.filter(mvp.name==formname)
	deadmvpdetails = deadmvp.query.filter(mvp.name==formname)
	
	for details in mvpdetails:
		lowtime = details.lowertime
		uptime = details.uppertime

	
	reslow =  (now + timedelta(minutes=int(lowtime))).strftime("%H:%M")
	resup  =  (now + timedelta(minutes=int(uptime))).strftime("%H:%M")
	

	return render_template('mvpdb.html', mvpdetails = mvpdetails, dietime = dietime, reslow = reslow, resup= resup, deadmvpdetails = deadmvpdetails)


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
