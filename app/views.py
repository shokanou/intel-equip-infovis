from flask import render_template,Flask,jsonify,request,url_for
import os
import sys
import glob
import string,re

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

def get_title(category):
	dot = '.'
	if category == 'j-rock':
		path = 'rock/'
	else:
		path = 'tpop/'
	title=[]
	BASE_DIR = '/Users/Ousyoukan/Desktop/microblog/app'
	file_path = BASE_DIR + '/static/data/'+category+'/*.mp3'
	file_path1 = BASE_DIR + '/static/data/'+category+'/'
	for filename in glob.glob(file_path):
		title1 = filename[:filename.index(dot)]
		title.append(title1[title1.index(path)+5:])
	return title


@app.route('/')
def nothing():
	return render_template("index.html")

@app.route('/vis')
def vis():
	return render_template("vis.html")


@app.route('/j-rock')
def j_rock():
	BASE_DIR = '/Users/Ousyoukan/Desktop/microblog/app'
	song = request.args.get('song','01',type=str)
	song_index = string.atoi(song)-1

	title = get_title('j-rock')
	file_path1 = BASE_DIR + '/static/data/j-rock/'
	lyric=open(file_path1+title[song_index]+'.txt').read()

	return render_template(
		"listen.html",
		lyric = lyric,
		title = title,
		song_index = song_index,
		category="j-rock",
		song=song)

@app.route('/britpop')
def britpop():
	BASE_DIR = '/Users/Ousyoukan/Desktop/microblog/app'
	song = request.args.get('song','01',type=str)
	song_index = string.atoi(song)-1
	title = get_title('britpop')
	file_path1 = BASE_DIR + '/static/data/britpop/'
	lyric=open(file_path1+title[song_index]+'.txt').read()


	return render_template(
		"listen.html",
		lyric = lyric,
		title = title,
		song_index = song_index,
		category="britpop",
		song=song)


app.route('/about')
def about():
	return render_template("about.html")

app.run(debug = True)


	