import Myui
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout, QMainWindow, QVBoxLayout, QLineEdit, QFormLayout, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Myui.Ui_start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
