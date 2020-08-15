import qtui
import sys
import option
import win32gui
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMessageBox, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout,QMainWindow,QVBoxLayout,QLineEdit,QFormLayout,QPushButton

class Ui_start(qtui.Ui_MainWindow): #定义一个ui类继承Qt Designer生成的类
    def __init__(self,Mainwindow):
        super().setupUi(Mainwindow) #初始化窗口
        self.Mainwindow = Mainwindow
        #self.action_2.clicked.connect(self.action2_solt)
        self.Mainwindow.setWindowIcon(QIcon('myico.ico'))    #设置窗口的图标
        self.Mainwindow.resize(300,300)
        self.label1 = QLabel(self.Mainwindow)  # 开始界面为窗口的说明界面 里面的控件及其排布
        self.TextBrowser1 = QTextBrowser(self.Mainwindow)
        self.label1.setText("<h2>使用说明</h2>")
        self.TextBrowser1.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.TextBrowser1.setText("1.在类别中选择自己想要打的副本\n"
                                  "2.点击")

        self.action_3.triggered.connect(self.action3_solt) #建立菜单栏和槽函数的connect
        self.layout_init()#布局
    def layout_init(self): #控件的排布函数
        self.widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label1)
        self.v_layout.addWidget(self.TextBrowser1)
        self.widget.setLayout(self.v_layout)
        self.Mainwindow.setCentralWidget(self.widget)

    def action3_solt(self):  #双人的菜单点击槽函数
        self.widget.setParent(None)
        label1 = QLabel("窗口1的句柄",self.Mainwindow)
        label2 = QLabel("窗口2的句柄",self.Mainwindow)
        label3 = QLabel("hwnd的值为: ",self.Mainwindow)

        # = option.GetMousePosition()
        label4 = QLabel("暂无数据",self.Mainwindow)
        label5 = QLabel("进程标题： ",self.Mainwindow)
        label6 = QLabel("暂无数据",self.Mainwindow)

        t = threading.Thread(target=lambda: thead_SetHwndLabel(label4, label6))
        t.start()
        label7 = QLabel("每轮时间", self.Mainwindow)
        label8 = QLabel("开车窗口", self.Mainwindow)

        line1 = QLineEdit(self.Mainwindow)
        line1.setMaximumWidth(100)
        line2 = QLineEdit(self.Mainwindow)
        line2.setMaximumWidth(100)
        line3 = QLineEdit(self.Mainwindow)
        line3.setMaximumWidth(100)
        line4 = QLineEdit(self.Mainwindow)
        line4.setMaximumWidth(100)
        line4.setPlaceholderText("填写数字1或者2")

        confirm_button = QPushButton('开始', self.Mainwindow)
        confirm_button.clicked.connect(lambda :self.action3_confirm(line1,line2,line3,line4))
        self.cancel_button = QPushButton('停止', self.Mainwindow)
        cancel_button =  self.cancel_button

        f_layout = QFormLayout()  # 1
        s_layout = QHBoxLayout()
        ss_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        all_v_layout = QVBoxLayout()

        s_layout.addWidget(label3)
        s_layout.addWidget(label4)
        ss_layout.addWidget(label5)
        ss_layout.addWidget(label6)
        f_layout.addRow(label1,line1)
        f_layout.addRow(label2, line2)
        f_layout.addRow(label7,line3)
        f_layout.addRow(label8, line4)
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(cancel_button)
        all_v_layout.addLayout(s_layout)
        all_v_layout.addLayout(ss_layout)
        all_v_layout.addLayout(f_layout)
        all_v_layout.addLayout(button_layout)
        widget = QWidget()
        widget.setLayout(all_v_layout)
        self.Mainwindow.setCentralWidget(widget)


    def action3_confirm(self,line1,line2,line3,line4):
        hwnd1 = line1.text()
        hwnd2 = line2.text()
        Turntime = line3.text()
        num = line4.text()
        if hwnd1 != "" and hwnd2 !="" and Turntime != "":   #判断是不是都是空的 只有不为空才能往下
            windows1=option.MyWindows(int(hwnd1))
            windows2=option.MyWindows(int(hwnd2))

            if windows1.ChangeWindows(10, 10, 500, 500) == 1:
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄1有误')
                return
            if windows2.ChangeWindows(10, 520, 500, 500) == 1:
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄2有误')
                return
            if num != "1" and num != "2":
                QMessageBox.information(self.Mainwindow, '提示', '请输入数字1或2')
                return

            self.clicktread = threading.Thread(target=lambda: thead_MouseClick(windows1, windows2, num, Turntime,2))
            self.clicktread.start()
            self.cancel_button.clicked.connect(self.action3_cancel)

        else:
            QMessageBox.information(self.Mainwindow, '提示', '请勿输入为空')
    def action3_cancel(self):
        option.stop_thread(self.clicktread)
        self.cancel_button.clicked.disconnect(self.action3_cancel)
        QMessageBox.information(self.Mainwindow, '提示', '成功停止！')

            
def thead_SetHwndLabel(label1,label2):  #线程函数
    while 1:
        hwnd = option.GetWindowHwnd()
        label1.setText(str(hwnd))
        label2.setText(str(win32gui.GetWindowText(hwnd)))

def thead_MouseClick(window1,window2,num,time,flag):
    if flag == 2:
        print(1)
        option.turn_two(window1, window2)
        while (1):
            option.snake_two(window1, window2, num, time)
            print(1)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui=Ui_start(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

