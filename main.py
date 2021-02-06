import tkinter as tk
import option
import Myui
import threading
import qtui
import sys
import option
import win32gui
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout, QMainWindow, QVBoxLayout, QLineEdit, QFormLayout, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Myui.Ui_start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
