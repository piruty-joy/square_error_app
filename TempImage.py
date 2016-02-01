from matplotlib.backends.backend_agg import FigureCanvasAgg
import os


class TempImage(object):

	def __init__(self, file_name, image):
		self.file_name = file_name
		self.image = image

	def create_png(self):
		canvas = FigureCanvasAgg(self.image)
		canvas.print_figure(self.file_name)

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		os.remove(self.file_name)
