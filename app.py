# coding: utf-8

from flask import Flask, send_file
import numpy
from matplotlib import pyplot
import string
import random
import TempImage
import square_error


app = Flask(__name__)


def plot(image):
	x = numpy.linspace(0, 10)
	y = numpy.sin(x)
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


@app.route('/')
def index():
	return '<img src="image.png">'

if __name__ == '__main__':
	app.run()
