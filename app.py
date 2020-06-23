#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import re
from flask import Flask
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def start():
	return render_template('startPage.html')

@app.route('/urlInputPage')
def urlInputPage():
	return render_template('urlInput.html')

@app.route('/fileInputPage')
def fileInputPage():
	return render_template('fileInput.html')

@app.route('/urlUpload', methods = ['POST'])
def info():
	error = None
	if request.method == 'POST':
		inputurl = request.form['url']
		str = inputurl
		#url = str		
		res = requests.get(str)
		html = BeautifulSoup.find(res.content, "html.parser")		
		return render_template('info.html', url=inputurl, parsed_page=html)

@app.route('/fileUpload', methods = ['POST'])
def fileUpload():
	if request.method == 'POST':	
		f = request.files['file']
		fo = open(f.filename,"r")
		lines = fo.readlines()
		l = len(lines)
		htmlList = list()
		for i in range(0,2):
			url = lines[i]
			str = url			
			res = requests.get(str)
			html = BeautifulSoup(res.content, "html.parser")
			tmp = html.find_all(string=True)
			htmlList.append(tmp)
		return render_template('upload.html', parsed_page = htmlList)


if __name__ == '__main__':
	app.run(debug=True);
