import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt6 import QtWidgets, QtCore
import numpy as np
import design
import collections
import psutil

t = np.arange(0.0, 1.0, 0.001)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.horizontalSlider.valueChanged.connect(lambda x: self.foo(x))
        self.horizontalSlider.valueChanged.connect(self.foo)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.insertWidget(0, self.canvas)

        ax = self.figure.add_subplot(111)
        self.update_plot()
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def foo(self):

        return self.data


    data=[]
    def update_plot(self):
        global data
        data_len=1
        # обработчик изменения значения слайдера
        #self.data = collections.deque(maxlen=data_len)
        for i in range(data_len):
            self.data.append(int(psutil.cpu_percent(1)))
        plt.cla()
        #data = self.foo()
        plt.plot(self.data, 'r-')
        plt.grid()
        self.canvas.draw()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()