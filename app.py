# coding: utf-8

from flask import Flask, send_file, render_template, request, jsonify
import numpy as np
from matplotlib import pyplot
import string
import random
import TempImage
import square_error
import json


app = Flask(__name__)


def plot(image):
	x = np.linspace(0, 10)
	y = np.sin(x)
	pyplot.plot(x, y)
	pyplot.savefig(image, format('png'))


@app.route('/image')
def error_graph():
	image = square_error.make_picture()
	chars = string.digits + string.ascii_letters
	img_name = ''.join(random.choice(chars) for i in range(64)) + '.png'
	
	with TempImage.TempImage(img_name, image) as img:
		img.create_png()
		return send_file(img_name, mimetype='image/png')


@app.route('/start')
def show_start_page():
	return render_template('index.html')


@app.route('/show', methods=['POST'])
def show():
	num = int(request.form['num'])
	function = np.sin if request.form['function'] == 'sin' else np.cos
	image = square_error.make_picture(num=num, function=function)
	chars = string.digits + string.ascii_letters
	img_name = ''.join(random.choice(chars) for i in range(64)) + '.png'

	with TempImage.TempImage(img_name, image) as img:
		img.create_png()
		return send_file(img_name, mimetype='image/png')


@app.route('/postText', methods=['POST'])
def lower_conversion():
	text = request.json['text']
	if "ping" in text:
		return_data = {"result": "pong"}
		return jsonify(ResultSet=json.dumps(return_data))
	lower_text = text.lower()
	print(lower_text)
	return_data = {"result": lower_text}
	return jsonify(ResultSet=json.dumps(return_data))


@app.route('/')
def index():
	return '<img src="image.png">'


if __name__ == '__main__':
	app.run()
