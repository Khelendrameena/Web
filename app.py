from datetime import datetime
import requests
import random
import json
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for,session, make_response
import smtplib
from email.mime.multipart import MIMEMultipart
import sqlite3
import numpy as np

# Connect to a database (will be created if it doesn't exist)

# Create a cursor object
from email.mime.text import MIMEText


from flask_session import Session
 
import uuid


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

	
quary = "jee"
url = f"https://newsapi.org/v2/everything?q={quary}&apiKey=a26e90658ca8499ca068782aa2179116"
response = requests.get(url)
id_array = []
data = response.json()
main = ["hay","hello"]
views_array = []

@app.route('/')
def index_1():
	 username = session.get("username")
	 if username:
	 	return redirect(f"/home/profile/{username}")
	 time_2 = []
	 for id in data["articles"]:
	 	if isinstance(id, dict):  # Check if id is a dictionary
	 		id["views"] = sum([i[2] if i[2] is not None else 0 for i in read_record("user.db", "views") if id["publishedAt"] == i[1]])
	 		time_2.append(int(''.join(id["publishedAt"].split('T')[0].split('-'))))
	 	else:
	 		print(f"Unexpected data format:")
	 time_4 = []
	 for i in range(0,len(time_2)):
	 	time_4.append(str(np.argmax(time_2)))
	 	time_2[np.argmax(time_2)] = 0
	 data["articles"].append(time_4)
	 	 					 			
	 time = datetime.now().year
	 return render_template('index.html',data=data["articles"],time = time,time_4=time_4)



