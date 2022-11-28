from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

im = Image.open('image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])

x = np.arange(0, im.width)
X = np.array([x, x ** 2.0, x ** 3.0, x ** 4.0, x ** 5.0]).transpose()

y = data[0, :, 2]

r, g, b = 0, 0, 0
r = data[0, :, 0]
g = data[0, :, 1]
b = data[0, :, 2]

lm = linear_model.LinearRegression()
lm.fit(X, b)
predicted_b = lm.predict(X)

lm = linear_model.LinearRegression()
lm.fit(X,r)
predicted_r = lm.predict(X)

lm = linear_model.LinearRegression()
lm.fit(X, g)
predicted_g = lm.predict(X)

fig, axs = plt.subplots(nrows= 3 , ncols= 1 )

axs[0].plot(np.arange(1, len(predicted_b) + 1), predicted_b, 'b-', linewidth  = 0.6)
axs[0].plot(np.arange(1, len(b) + 1), b, '-', color = '#0a0b0c3a', linewidth  = 0.6)

axs[1].plot(np.arange(1, len(predicted_g) + 1), predicted_g, 'g-', linewidth  = 0.6)
axs[1].plot(np.arange(1, len(g) + 1), g, '-', color = '#0a0b0c3a', linewidth  = 0.6)

axs[2].plot(np.arange(1, len(predicted_r) + 1), predicted_r, 'r-', linewidth  = 0.6)
axs[2].plot(np.arange(1, len(r) + 1), r, '-', color = '#0a0b0c3a', linewidth  = 0.6)
plt.grid()
plt.show()


plt.plot(data[0, :, 0], 'r', data[0, :, 1], 'g', data[0, :, 2], 'b')
plt.xlim(0, 1200)
plt.ylim(0, 250)
plt.grid()
plt.show()

def compression(channel):
    lm = linear_model.LinearRegression()
    lm.fit(X, channel)
    predicted = lm.predict(X)
    #diff = channel - predicted
    diff=channel - predicted
    bits_per_channel = 4
    threshold = 2 ** (bits_per_channel - 1) - 1
    clip = np.clip(diff, -threshold, threshold)
    channel = predicted + clip
    for i in range(len(channel)):
        if channel[i] < 0:
            channel[i] = 0
    return channel
r, g, b = 0, 0, 0
pix = im.load()
for i in range(im.height):
    r = data[i, :, 0]
    g = data[i, :, 1]
    b = data[i, :, 2]
    rr = compression(r)
    gg = compression(g)
    bb = compression(b)
    for j in range(im.width):
        lst = list(pix[j,i])
        lst[0] = int(rr[j])
        lst[1] = int(gg[j])
        lst[2] = int(bb[j])
        pix[j,i] = tuple(lst)

im.save('ready.png')
