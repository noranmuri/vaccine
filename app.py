#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import re
import pandas as pd
import shutil
import jinja2
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

# 서버 url이나 파일 받는 코드

@app.route('/urlInputDef')
def urlInputPDef():
	return render_template('urlInputPage.html')

@app.route('/fileInputDef')
def fileInputDef():
	return render_template('fileInputPage.html')

# 크롤링 하는 코드

@app.route('/urlUploadDef', methods = ['POST'])
def urlUploadDef():
	error = None
	if request.method == 'POST':
		inputurl = request.form['url']
		str = inputurl
		#url = str		
		res = requests.get(str)
		html = BeautifulSoup(res.content, "html.parser")	
		return render_template('infoPage.html', parsed_page=html)

@app.route('/fileUploadDef', methods = ['POST'])
def fileUploadDef():
	if request.method == 'POST':	
		file = request.files['file']
		#file = open(f.filename, 'r')
		lines = file.readlines()
		l = len(lines)
		htmlList = list()
		#url = list()
		#crawling = list()
		for i in range(0,2):
			url = lines[i]
			str = url			
			res = requests.get(str)
			html = BeautifulSoup(res.content, "html.parser")
			tmp = html.find_all(string=True)
			htmlList.append(html)
		df_marks = pd.DataFrame({'url':lines, 'data':htmlList})
		file = open("data.html", "w+")
		file.write("""<!DOCTYPE html PUBLIC "-//w3c//DTD HTML 4.0 Transitional//EN">\n""")
		file.write("""<html>\n\t<head></head>\n\t<body>\n""")
		tablehtml = df_marks.to_html()
		file.write(tablehtml)
		file.write("""\n\t</body>\n</html>""")

		filename = 'data.html'
		src = '/home/yoon/'
		dir = '/home/yoon/templates/'
		shutil.move(src+filename, dir+filename)
		return render_template('data.html')

# main

if __name__ == '__main__':
	app.run(debug=True);
