from flask import Flask ,render_template ,request
import sys
from dbconnect import connection
import gc

row=[3,3,4,4,5,6,10]
col=[3,4,4,5,5,6,10]
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('regular.html',h=2,r=2)
@app.route('/regular/<int:t>')
def regular(t):
	h=row[t-1]
	r=col[t-1]
	return render_template('regular.html',h=h,r=r)
@app.route('/star/<int:t>')
def star(t):
	h=row[t-1]
	r=col[t-1]
	return render_template('star.html',h=h,r=r)
@app.route('/flower/<int:t>')
def flower(t):
	h=row[t-1]
	r=col[t-1]
	return render_template('flower.html',h=h,r=r)
@app.route('/straight/<int:t>')
def straight(t):
	h=row[t-1]
	r=col[t-1]
	return render_template('straight.html',h=h,r=r)
@app.route('/curve/<int:t>')
def curve(t):
	h=row[t-1]
	r=col[t-1]
	return render_template('curve.html',h=h,r=r)
@app.route('/thankyou',methods=["GET","POST"])
def thankyou():
	return render_template('thankyou.html')
@app.route('/data',methods=["GET","POST"])
def data():
	if request.method=="POST":
		data=request.get_json()
		# print(data)
		time=data["mydata"][0]["time"]
		gender=data["mydata"][1]["gender"]
		age=data["mydata"][2]["age"]
		shape=data["mydata"][3]["shape"]
		rsize=data["mydata"][4]["rsize"]
		csize=data["mydata"][5]["csize"]
		clicks=data["mydata"][6]["clicks"]
		c,conn=connection()
		c.execute("INSERT INTO info (gender,time,age,shape,rsize,csize,clicks) VALUES (%s, %s, %s, %s,%s,%s,%s)",(gender,time,age,shape,rsize,csize,clicks))
		conn.commit()
		c.close()
		conn.close()
		gc.collect()
	return render_template('thankyou.html')




if __name__ == "__main__":
    app.run()