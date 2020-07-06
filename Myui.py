import qtui
import sys
import option
import win32gui
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout,QMainWindow,QVBoxLayout,QLineEdit,QFormLayout

class Ui_start(qtui.Ui_MainWindow): #定义一个ui类继承Qt Designer生成的类
    def __init__(self,Mainwindow):
        super().setupUi(Mainwindow) #初始化窗口
       # self.Mainwindow = Mainwindow
        #self.action_2.clicked.connect(self.action2_solt)
        Mainwindow.setWindowIcon(QIcon('myico.ico'))    #设置窗口的图标
        Mainwindow.resize(300,300)
        self.label1 = QLabel(Mainwindow)  # 开始界面为窗口的说明界面 里面的控件及其排布
        self.TextBrowser1 = QTextBrowser(Mainwindow)
        self.label1.setText("<h2>使用说明</h2>")
        self.TextBrowser1.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.TextBrowser1.setText("1.在类别中选择自己想要打的副本\n"
                                  "2.点击")

        self.action_3.triggered.connect(lambda :self.action3_solt(Mainwindow)) #建立菜单栏和槽函数的connect
        self.layout_init(Mainwindow)#布局
    def layout_init(self,Mainwindow): #控件的排布函数
        self.widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label1)
        self.v_layout.addWidget(self.TextBrowser1)
        self.widget.setLayout(self.v_layout)
        Mainwindow.setCentralWidget(self.widget)

    def action3_solt(self,Mainwindow):  #双人的菜单点击槽函数
        self.widget.setParent(None)
        label1 = QLabel("窗口1的句柄",Mainwindow)
        label2 = QLabel("窗口2的句柄",Mainwindow)
        label3 = QLabel("hwnd的值为: ",Mainwindow)

        # = option.GetMousePosition()
        label4 = QLabel("暂无数据",Mainwindow)
        line1 = QLineEdit(Mainwindow)
        line1.setMaximumWidth(100)
        line2 = QLineEdit(Mainwindow)
        line2.setMaximumWidth(100)

        f_layout = QFormLayout()  # 1
        s_layout = QHBoxLayout()
        all_v_layout = QVBoxLayout()

        s_layout.addWidget(label3)
        s_layout.addWidget(label4)
        f_layout.addRow(label1,line1)
        f_layout.addRow(label2, line2)
        all_v_layout.addLayout(s_layout)
        all_v_layout.addLayout(f_layout)
        widget = QWidget()
        widget.setLayout(all_v_layout)
        Mainwindow.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui=Ui_start(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())


#class father():
