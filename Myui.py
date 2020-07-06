import qtui
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout,QMainWindow,QVBoxLayout

class Ui_start(qtui.Ui_MainWindow):
    def __init__(self,Mainwindow):
        super().setupUi(Mainwindow)
       # self.Mainwindow = Mainwindow
        #self.action_2.clicked.connect(self.action2_solt)
        MainWindow.setWindowIcon(QIcon('myico.ico'))
        self.label1 = QLabel(Mainwindow)  # 2
        self.TextBrowser1 = QTextBrowser(Mainwindow)
        self.label1.setText("<h2>使用说明</h2>")
        self.TextBrowser1.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.TextBrowser1.setText("1.在类别中选择自己想要打的副本\n"
                                  "2.点击")

        self.action_2.triggered.connect(self.action2_solt)
        self.layout_init(Mainwindow)
    def layout_init(self,Mainwindow):
        self.widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label1)
        self.v_layout.addWidget(self.TextBrowser1)
        self.widget.setLayout(self.v_layout)
        Mainwindow.setCentralWidget(self.widget)

    def action2_solt(self,Mainwindow):
        self.widget.setParent(None)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui=Ui_start(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())


#class father():
