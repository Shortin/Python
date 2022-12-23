import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QTableWidgetItem,QGridLayout
from PyQt6.QtWidgets import QMainWindow, QLabel, QFileDialog,QHBoxLayout,QTableWidget
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('task6.ui', self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        name = self.lineEdit_Name.text()
        number = self.lineEdit_Number.text()
        table=self.tableWidget_1
        rows = table.rowCount()
        table.setRowCount(rows+1)
        table.setItem(rows, 0, QTableWidgetItem(name))
        table.setItem(rows, 1, QTableWidgetItem(number))
        table.resizeColumnsToContents()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

