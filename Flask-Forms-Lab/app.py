from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Kareen","Samer", "George", "Fouad", "Alice"]


@app.route('/login',methods=["POST","GET"])  # '/' for the default page
def login():
  if request.method == "GET":
  	return render_template('login.html')
  else :
  	name = request.form['username']
  	user_password = request['password']
  	if username == name and user_password == password:
  		return render_template('home.html',username = name,password = user_password)
  		
  return render_template('login.html')
  	
@app.route('/home',methods=["POST","GET"])
def home():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:name>',methods=['GET','POST'])
def friend_exists(name):
	return render_template(
        'friend_exists.html', n = name)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)