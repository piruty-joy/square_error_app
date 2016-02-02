# coding: utf-8

import random
import string

import numpy as np
from flask import Flask, send_file, render_template, request

import TempImage
import square_error

app = Flask(__name__)


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


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
