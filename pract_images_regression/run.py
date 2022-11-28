from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


im = Image.open('image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])

x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

#Отобразить графики ниже
y = data[0, :, 2]

plt.plot(np.arange(1, len(y) + 1), y, 'r-')
plt.title('Ошибка при повторении')
plt.xlabel('номер итерации')
plt.ylabel('уровень ошибки')
plt.grid()
plt.show()
#