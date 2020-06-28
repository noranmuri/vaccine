#!/usr/bin/python
#-*- coding: utf-8 -*-

from konlpy.tag import Twitter
from collections import Counter
import copy
import os
import time
import re
import pandas as pd
import shutil
import jinja2
from flask import Flask
from flask import render_template, send_from_directory, url_for
from flask import request
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def start():
	return render_template('startPage.html')

#url을 받는 page로 연결
@app.route('/urlInputDef')
def urlInputPDef():
	return render_template('urlInputPage.html')

#url 파일을 받는 page로 연결
@app.route('/fileInputDef')
def fileInputDef():
	return render_template('fileInputPage.html')

# 입력된 url을 가지고 크롤링 하여 결과를 나타내는 페이지로 연결
def count(line):
	
	inputurl = request.form['url']
	str = inputurl
	res = requests.get(str)
	html = BeautifulSoup(res.content,"html.parser")
	tmp = html.get_text()
		
	noun = tmp.split()
	c = Counter(noun)

	return len(c)

# 입력된 url을 가지고 크롤링 하여 결과를 나타내는 페이지로 연결
@app.route('/urlUploadDef', methods = ['POST'])
def urlUploadDef():
	error = None
	if request.method == 'POST':
		start=time.time()
		inputurl = request.form['url']
		str = inputurl
		state = 'success'
		res = requests.get(inputurl)
		html = BeautifulSoup(res.content, "html.parser")
		t = time.time() - start
		c = count(inputurl)
		return render_template('infoPage.html',  c=c, t=t, state=state, inputurl=inputurl)

@app.route('/repeatUrl', methods = ['POST'])
def repeatPageurl():
	if request.method == 'POST':
		start = time.time()
		url = request.form['url']
		res = requests.get(url)
		html = BeautifulSoup(res.content, "html.parser")
		run = time.time() - start
		c = count(inputurl)
		state = "change"
		return render_template('infoPage.html', c=c, t=run, state = state, inputurl=url)

# 단어 수 체크하여 튜플 리스트로 반환
def countNoun(url):
	start = time.time()
	res = requests.get(url)
	html = BeautifulSoup(res.content, "html.parser")
	tmp = html.get_text()	# tmp는 문자열로만 이루어진 정돈된 문자열 리스트
	nouns = tmp.split()
	count = Counter(nouns)  # 단어와 빈도수의 튜플로 이루어진 리스트
	run = time.time()-start
	return count,run

@app.route('/repeatPage', methods = ['POST'])
def repeatPage():
	if request.method == 'POST':
		index = request.form['index']
		list = request.form['list']
		return render_template('ex.html', index = index, list = list)
		#return render_template('example.html',index = index, url = url, list = List)
		element = List[index]		
		url = element['url']	#url
		count, run = countNoun(url)
		List[index] = (index, url, count, run)
		#return render_template('table.html',list = List)

# 입력받은 파일을 크롤링하여 표가 있는 페이지로 연결
@app.route('/fileUploadDef', methods = ['POST'])
def fileUploadDef():
	if request.method == 'POST':
		file = request.files['file']
		#file = open(f.filename, 'r')
		lines = file.readlines()
		l = len(lines)
		List = list()					# List ( index, url, noun count, time )
		state = "success"	
		
		for i in range(0,l):
			if lines[i] not in lines:
				state = "overlap"
				List.append(
					{
					"index":i,
					"url":lines[i],
					"len":0,
					"words":0,
					"time":0,
					"state":state,
					}			
				)		
			else:
				#spliter = Twitter()				
				lines[i] = lines[i].decode('ascii')
				start = time.time()
				res = requests.get(lines[i])
				html = BeautifulSoup(res.content, "html.parser")	
				tmp = html.get_text()	# tmp는 문자열로만 이루어진 정돈된 문자열 리스트
				nouns = tmp.split()
				#return render_template('ex.html', url = nouns)
				count = Counter(nouns)				
				"""return_list = []
				for n,c in count.most_common(10):
					temp = {'tag':n, 'count':c}
					return_list.append(temp)				
				#count = Counter(nouns) # 단어와 빈도수의 튜플로 이루어진 리스트"""
				run = time.time()-start
				List.append(	
					{
						"index":i,
						"url":lines[i],
						"len":len(count),
						"words":count,
						"time":run,
						"state":state,
					}			
				)
		
		return render_template('table.html', list = List)

@app.route('/top10Page', methods = ['POST'])
def top10Page():
	list = request.form['list']
	url = request.form['url']
	#return render_template('ex.html', url = list)
	return render_template('top10Page.html', list = list, url = url)
# main
if __name__ == '__main__':
	app.run(debug=True);
