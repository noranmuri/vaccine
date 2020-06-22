#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
from flask import Flask
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def start():
	return render_template('fileInput.html')

@app.route('/info', methods = ['POST'])
def info():
	error = None
	if request.method == 'POST':
		inputurl = request.form['url']
		str = inputurl
		url = str
		res = requests.get(url)
		html = BeautifulSoup(res.content, "html.parser")		
	return render_template('info.html',url=myurl,parsed_page=html)

@app.route('/fileUpload',methods = ['POST'])
def fileUpload():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return render_template('upload.html')	



if __name__ == '__main__':
	app.run();
