import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QFileDialog,QHBoxLayout
import re
from collections import Counter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('test2.ui', self)
        self.button_openFile.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Выберите текстовый файл', 'D:\\', 'Текстовые файлы (*.txt)')[0]
        self.textEdit.setText(filename)
        #text = self.textEdit.toPlainText()
        with open(filename, 'r') as txt_file:
            data = txt_file.read()
        d = {}
        symbols = (symbol for line in data for symbol in re.findall(r'\w', line))
        for symbol, count in Counter(symbols).most_common():
            d[symbol] = count
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        #self.verticalLayout.deleteLater()
        self.verticalLayout.insertWidget(0, self.canvas)
        ax = self.figure.add_subplot(111)
        ax.bar(*zip(*sorted(d.items())))
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

