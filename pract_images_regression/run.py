from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


im = Image.open('image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])

x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

#Отобразить графики ниже
channel_1 = data[0, :, 2]
channel_2 = data[0, :, 1]
channel_3 = data[0, :, 0]

# plt.plot(np.arange(1, len(channel_1) + 1), channel_1, 'b-', linewidth  = 0.8)
# plt.plot(np.arange(1, len(channel_2) + 1), channel_2, 'g-', linewidth  = 0.8)
# plt.plot(np.arange(1, len(channel_3) + 1), channel_3, 'r-', linewidth  = 0.8)
# plt.title('Цветовые каналы, первой строки')
# plt.grid()
# plt.show()
#
def SadesCurve(X, channel):
	lm = linear_model.LinearRegression()
	lm.fit(X, channel)
	predicted = lm.predict(X)

	plt.plot(np.arange(1, len(predicted) + 1), predicted, 'b-', linewidth  = 0.8)
	plt.plot(np.arange(1, len(channel) + 1), channel, '-', color = '#0a0b0c3a', linewidth  = 0.8)
	plt.title('кривая оттенков')
	plt.grid()
	plt.show()


lm = linear_model.LinearRegression()
lm.fit(X, channel_1)
predicted = lm.predict(X)

difference = channel_1 - predicted#Разности

bits_per_channel = 4
threshold = 2**(bits_per_channel - 1) - 1

clip = np.clip(difference, -threshold, threshold)
y = predicted + clip

pix = im.load()
осталось написать цыкл чтобы их все закодировать
print(y)