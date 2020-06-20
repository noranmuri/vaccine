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
	error = None
	if request.method == 'POST':
		file = request.files['file']
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			a = 'file uploaded'
	return render_template('upload.html', data = a)



if __name__ == '__main__':
	app.run();
