# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

from numpy.random import normal


N = 10  # サンプルのデータ数
M = [0, 1, 3, 9]  # 多項式の次数


# データセットの準備
def create_dataset(num):
	dataset = DataFrame(columns=['x', 'y'])
	for i in range(num):
		x = float(i) / float(num - 1)
		y = np.cos(2 * np.pi * x) + normal(scale=0.3)
		dataset = dataset.append(Series([x, y], index=['x', 'y']), ignore_index=True)
	return dataset


# 平方根平均二乗誤差の計算
def rms_error(dataset, f):
	err = 0.0
	for index, line in dataset.iterrows():
		x, y = line.x, line.y
		err += 0.5 * (y - f(x)) ** 2
	return np.sqrt(2 * err / len(dataset))


# 最小二乗法で解を計算
def resolve(dataset, m):
	t = dataset.y
	phi = DataFrame()
	for i in range(0, m + 1):
		p = dataset.x ** i
		p.name = "x**%d" % i
		phi = pd.concat([phi, p], axis=1)
	tmp = np.linalg.inv(np.dot(phi.T, phi))
	ws = np.dot(np.dot(tmp, phi.T), t)

	def f(x):
		y = 0
		for i, w in enumerate(ws):
			y += w * (x ** i)
		return y

	return f, ws


def make_picture():
	train_set = create_dataset(N)
	df_ws = DataFrame()

	fig = plt.figure()
	for c, m in enumerate(M):
		f, ws = resolve(train_set, m)
		df_ws = df_ws.append(Series(ws, name="M=%d" % m))

		subplot = fig.add_subplot(2, 2, c + 1)
		subplot.set_xlim(-0.05, 1.05)
		subplot.set_ylim(-1.5, 1.5)
		subplot.set_title("M=%d" % m)

		subplot.scatter(train_set.x, train_set.y, marker='o', color='blue')

		linex = np.linspace(0, 1, 101)
		liney = np.cos(2 * np.pi * linex)
		subplot.plot(linex, liney, color='green', linestyle='--')

		linex = np.linspace(0, 1, 101)
		liney = f(linex)
		label = "E(RMS)=%.2f" % rms_error(train_set, f)
		subplot.plot(linex, liney, color='red', label=label)
		subplot.legend(loc=1)

	return fig

if __name__ == '__main__':
	fig = make_picture()
	fig.show()
