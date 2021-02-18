import qtui
import option
import win32gui
import threading
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout, QMainWindow, QVBoxLayout, QLineEdit, QFormLayout, QPushButton
from PyQt5.QtCore import QTimer
import time
class Ui_start(qtui.Ui_MainWindow):  # 定义一个ui类继承Qt Designer生成的类
    def __init__(self, Mainwindow):
        self.Mainwindow = Mainwindow
        super().setupUi(self.Mainwindow)  # 初始化窗口
        # self.action_2.clicked.connect(self.action2_solt)
        self.Mainwindow.setWindowIcon(
            QIcon('img/necessary/myico.ico'))  # 设置窗口的图标
        self.Mainwindow.resize(300, 300)
        self.Mainwindow.setFixedSize(300, 300)  # 设置窗口大小
        self.label1 = QLabel(self.Mainwindow)  # 开始界面2为窗口的说明界面 里面的控件及其排布
        self.TextBrowser1 = QTextBrowser(self.Mainwindow)
        self.label1.setText("<h2>使用说明</h2>")
        self.TextBrowser1.setStyleSheet(
            "QTextBrowser{border-width:0;border-style:outset}")
        self.TextBrowser1.setText("1.在类别中选择自己想要打的副本,和开黑人数\n"
                                  "2.你需要先填写句柄号码（窗口代号）会有显示\n"
                                  "3.填写好等待的时间和开车的窗口号码\n"
                                  "4.点击开始即可！需要停止的时候可以点击停止！\n"
                                  "PS:你需要组队打完第一把之后，也就是默认邀请的阶段\n")

        self.layout_init()  # 主界面布局
        self.singleConnect()


    def singleConnect(self):
        self.action_3.triggered.connect(self.action3_solt)  # 双人御魂子界面connect
        self.action_3.triggered.connect(lambda: print(1))
        self.action_9.triggered.connect(self.action9_solt)  # 点击指定地点子界面connect
        self.action_9.triggered.connect(lambda: print(1))
    def layout_init(self):  # 控件的排布函数
        self.widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label1)
        self.v_layout.addWidget(self.TextBrowser1)
        self.widget.setLayout(self.v_layout)
        self.Mainwindow.setCentralWidget(self.widget)

    def action3_solt(self): #双人御魂
        print(2)
        action3 = DoubleYuHun(self.Mainwindow)
    def action9_solt(self): #点击指定地点
        print(3)
        action9 = SelectedPlace(self.Mainwindow)


class DoubleYuHun(Ui_start):
    def __init__(self,oldWindows):

        self.Mainwindow = oldWindows
        self.turnTimes = 0

        # self.widget.setParent(None)
        self.label1 = QLabel("窗口1的句柄", self.Mainwindow)
        self.label2 = QLabel("窗口2的句柄", self.Mainwindow)
        self.label3 = QLabel("窗口句柄的值为: ", self.Mainwindow)
        self.label4 = QLabel("暂无数据", self.Mainwindow)
        self.label5 = QLabel("进程标题： ", self.Mainwindow)
        self.label6 = QLabel("暂无数据", self.Mainwindow)
        self.label7 = QLabel("每轮时间(秒)", self.Mainwindow)
        self.label8 = QLabel("开车窗口", self.Mainwindow)
        self.label9 = QLabel("已经打了:", self.Mainwindow)
        self.label10 = QLabel("0轮", self.Mainwindow)

        self.line1 = QLineEdit(self.Mainwindow)
        self.line1.setMaximumWidth(100)
        self.line2 = QLineEdit(self.Mainwindow)
        self.line2.setMaximumWidth(100)
        self.line3 = QLineEdit(self.Mainwindow)
        self.line3.setMaximumWidth(100)
        self.line4 = QLineEdit(self.Mainwindow)
        self.line4.setMaximumWidth(100)
        self.line4.setPlaceholderText("数字1或者2")

        self.confirm_button = QPushButton('开始', self.Mainwindow)
        self.confirm_button.clicked.connect(self.test1)
        #self.confirm_button.clicked.connect(lambda :self.test1())
        self.cancel_button = QPushButton('停止', self.Mainwindow)

        f_layout = QFormLayout()  # 1
        s_layout = QHBoxLayout()
        ss_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        turnsLayout = QHBoxLayout()
        all_v_layout = QVBoxLayout()

        s_layout.addWidget(self.label3)
        s_layout.addWidget(self.label4)
        ss_layout.addWidget(self.label5)
        ss_layout.addWidget(self.label6)
        turnsLayout.addWidget(self.label9)
        turnsLayout.addWidget(self.label10)
        f_layout.addRow(self.label1, self.line1)
        f_layout.addRow(self.label2, self.line2)
        f_layout.addRow(self.label7, self.line3)
        f_layout.addRow(self.label8, self.line4)

        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        all_v_layout.addLayout(s_layout)
        all_v_layout.addLayout(ss_layout)
        all_v_layout.addLayout(f_layout)
        all_v_layout.addLayout(turnsLayout)
        all_v_layout.addLayout(button_layout)

        self.widget = QWidget()
        self.widget.setLayout(all_v_layout)
        self.Mainwindow.setCentralWidget(self.widget)

        #self.labelChange = threading.Thread(target=lambda :thead_SetHwndLabel(self.label4, self.label6))
        #self.labelChange.start()
    def test1(self):
        print(2)

    def action3_confirm(self):
        hwnd1 = self.line1.text()
        hwnd2 = self.line2.text()
        turnTimeEach = self.line3.text()
        num = self.line4.text()

        if hwnd1 != "" and hwnd2 != "" and turnTimeEach != "":  # 判断是不是都是空的 只有不为空才能往下
            windows1 = option.MyWindows(int(hwnd1))
            windows2 = option.MyWindows(int(hwnd2))

            if windows1.ChangeWindows(10, 10, 840, 500) == 1:
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄1有误')
                return
            if windows2.ChangeWindows(10, 520, 840, 500) == 1:
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄2有误')
                return
            if num != "1" and num != "2":
                QMessageBox.information(self.Mainwindow, '提示', '请输入数字1或2')
                return

            self.clicktread = threading.Thread(target=lambda: self.action3_thead_MouseClick(
                windows1, windows2, num, turnTimeEach, 2))
            self.clicktread.start()
            self.cancel_button.clicked.connect(self.action3_cancel)
            self.confirm_button.clicked.disconnect()
            self.confirm_button.clicked.connect(self.action3_cannotClick)
        else:
            QMessageBox.information(self.Mainwindow, '提示', '请勿输入为空')

    def action3_cancel(self):
        option.stop_thread(self.clicktread)
        self.cancel_button.clicked.disconnect()
        self.confirm_button.clicked.connect(self.action3_confirm)
        self.confirm_button.clicked.disconnect(self.action3_cannotClick)
        self.turnTimes = 0
        self.label10.setText(str(self.turnTimes) + "轮")
        QMessageBox.information(self.Mainwindow, '提示', '成功停止！')

    def action3_cannotClick(self):
        QMessageBox.information(self.Mainwindow, '提示', '请先停止当前的点击！')

    # 动作线程
    def action3_thead_MouseClick(self, window1, window2, num, time, flag):
        if flag == 2:
            option.turn_two(window1, window2)
            while (1):
                self.turnTimes += 1
                option.snake_two(window1, window2, num, time)

class SelectedPlace(Ui_start):
    def __init__(self, oldWindows):
        self.Mainwindow = oldWindows
        self.label1 = QLabel("窗口句柄的值为: ", self.Mainwindow)
        self.label2 = QLabel("暂无数据", self.Mainwindow)
        self.label3 = QLabel("进程标题： ", self.Mainwindow)
        self.label4 = QLabel("暂无数据", self.Mainwindow)
        self.label5 = QLabel("窗口的句柄", self.Mainwindow)
        self.label6 = QLabel("每轮时间(秒)", self.Mainwindow)

        self.line1 = QLineEdit(self.Mainwindow)
        self.line1.setMaximumWidth(100)
        self.line2 = QLineEdit(self.Mainwindow)
        self.line2.setMaximumWidth(100)
        self.line2.setPlaceholderText("数字1或者2")

        self.confirm_button = QPushButton('开始', self.Mainwindow)
        #self.confirm_button.clicked.connect(self.action3_confirm)
        self.cancel_button = QPushButton('停止', self.Mainwindow)

        layout1 = QFormLayout() #负责显示左右一对一的
        buttonLayout = QHBoxLayout()
        layoutAll = QVBoxLayout()
        layout1.addRow(self.label1, self.label2)
        layout1.addRow(self.label3, self.label4)
        layout1.addRow(self.label5,self.line1)
        layout1.addRow(self.label6, self.line2)
        buttonLayout.addWidget(self.confirm_button)
        buttonLayout.addWidget(self.cancel_button)

        layoutAll.addLayout(layout1)
        layoutAll.addLayout(buttonLayout)

        self.widget = QWidget()
        self.widget.setLayout(layoutAll)
        self.Mainwindow.setCentralWidget(self.widget)


# 保持label标签同步线程函数
def thead_SetHwndLabel(label1,label2):
    try:
        oldHwnd = 0
        while(1):
            hwnd = option.GetWindowHwnd()
            if oldHwnd != hwnd:
                label1.setText(str(hwnd))
                label2.setText(str(win32gui.GetWindowText(hwnd)))
            oldHwnd = hwnd
            time.sleep(0.1)
    except:
        pass