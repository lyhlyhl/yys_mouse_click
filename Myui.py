import qtui
import option
import win32gui
import threading
import re
from PyQt5.QtGui import QIcon,QMouseEvent
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout, QMainWindow, QVBoxLayout, QLineEdit, QFormLayout, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
import pyautogui
import time
from signal import mySignal

global optionStaus #负责所有线程的停止
optionStaus = 0

class Ui_start(qtui.Ui_MainWindow):  # 定义一个ui类继承Qt Designer生成的类
    def __init__(self, Mainwindow):
        self.Mainwindow = Mainwindow
        super().setupUi(self.Mainwindow)  # 初始化窗口

        self.Mainwindow.setWindowIcon(
            QIcon('img/necessary/myico.ico'))  # 设置窗口的图标
        self.Mainwindow.resize(400, 400)
        self.Mainwindow.setFixedSize(400, 400)  # 设置窗口大小
        self.label1 = QLabel(self.Mainwindow)  # 开始界面2为窗口的说明界面 里面的控件及其排布
        self.TextBrowser1 = QTextBrowser(self.Mainwindow)
        self.label1.setText("<h2>使用说明</h2>")
        self.TextBrowser1.setStyleSheet(
            "QTextBrowser{border-width:0;border-style:outset}")
        self.TextBrowser1.setText("1.在类别中选择自己想要打的副本,和开黑人数\n"
                                  "2.你需要先填写句柄号码（窗口代号）会有显示\n"
                                  "3.填写好等待的时间和开车的窗口号码\n"
                                  "4.点击开始即可！需要停止的时候可以点击停止！\n"
                                  "PS:如果是多人你需要组队打完第一把之后，也就是默认邀请的阶段\n")

        self.layout_init()  # 主界面布局
        self.singleConnect()


    def singleConnect(self):   #信号连接函数
        self.action_3.triggered.connect(self.action3_solt)  # 双人御魂子界面connect
        self.action_9.triggered.connect(self.action9_solt)  # 点击指定地点子界面connect
    def layout_init(self):  # 控件的排布函数
        self.widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label1)
        self.v_layout.addWidget(self.TextBrowser1)
        self.widget.setLayout(self.v_layout)
        self.Mainwindow.setCentralWidget(self.widget)

    def action3_solt(self): #双人御魂
        global optionStaus
        if optionStaus == 0:
            action3 = DoubleYuHun(self.Mainwindow)
        else:
            QMessageBox.information(self.Mainwindow, '提示', '请先停止当前的点击！')
    def action9_solt(self): #点击指定地点
        global optionStaus
        if optionStaus == 0:
            action9 = SelectedPlace(self.Mainwindow)
        else:
            QMessageBox.information(self.Mainwindow, '提示', '请先停止当前的点击！')


class DoubleYuHun(Ui_start, QObject):
    def __init__(self,oldWindows):
        super(Ui_start, self).__init__()
        self.Mainwindow = oldWindows
        self.turnTimes = 0
        #下面一大坨都是布局用的和各种控件
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

        self.cancel_button = QPushButton('停止', self.Mainwindow)
        self.confirm_button = QPushButton('开始', self.Mainwindow)


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

        self.signalCancel = mySignal()    #自定义信号
        self.signalCancel.signalCancel.connect(self.action3_cancel) #取消信号的连接

        # 这里太离谱了，必须使用一个lambda之后才能connect成功
        self.confirm_button.clicked.connect(self.action3_confirm) #确认的槽信号

        #改变标签显示句柄用的线程函数
        self.labelChange = threading.Thread(target=lambda :thead_SetHwndLabel(self.label4, self.label6,None))
        self.labelChange.start()
    def action3_confirm(self):  #确认按键的槽函数

        hwnd1 = self.line1.text()
        hwnd2 = self.line2.text()
        turnTimeEach = self.line3.text()
        num = self.line4.text()
        print("确定点击")
        if hwnd1 != "" and hwnd2 != "" and turnTimeEach != "":  # 判断是不是都是空的 只有不为空才能往下
            windows1 = option.MyWindows(int(hwnd1))
            windows2 = option.MyWindows(int(hwnd2))

            # 1080显示的值840 500
            if windows1.ChangeWindows(10, 10, 1100, 665) == 1: #比例刚刚好这个比例，大概在1.6541左右
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄1有误')
                return
            if windows2.ChangeWindows(10, 670, 1100, 665) == 1:
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄2有误')
                return
            if num != "1" and num != "2":
                QMessageBox.information(self.Mainwindow, '提示', '请输入数字1或2')
                return

            self.clickTread = threading.Thread(target=lambda: self.action3_thead_MouseClick(
                windows1, windows2, num, turnTimeEach))
            self.clickTread.start()

            self.cancel_button.clicked.connect(lambda :self.action3_cancel("成功停止！"))
            self.confirm_button.clicked.disconnect()
            self.confirm_button.clicked.connect(self.action3_cannotClick)
        else:
            QMessageBox.information(self.Mainwindow, '提示', '请勿输入为空')

    def action3_cancel(self, text=None):
        global optionStaus
        optionStaus = 0
        print("取消点击")

        option.stop_thread(self.clickTread)
        self.cancel_button.clicked.disconnect()
        self.confirm_button.clicked.connect(self.action3_confirm)
        self.confirm_button.clicked.disconnect(self.action3_cannotClick)
        self.turnTimes = 0
        QMessageBox.information(self.Mainwindow, '提示', text)

    def action3_cannotClick(self):
        QMessageBox.information(self.Mainwindow, '提示', '请先停止当前的点击！')

    # 动作线程
    def action3_thead_MouseClick(self, window1, window2, num, time):
        global optionStaus
        optionStaus = 1
        option.turn_two(window1, window2)
        while (1):
            option.snake_two(window1, window2, num, time) # 得分离开来将一次事件
            self.turnTimes += 1
            self.label10.setText(str(self.turnTimes) + "轮")
            if self.turnTimes >= 100:
                self.signalCancel.signalCancel.emit("别刷辣别刷辣！我要累死了！")
            if pyautogui.locateOnScreen("./img/necessary/toomany.png",confidence = 0.6 ) is not None:
                self.signalCancel.signalCancel.emit("御魂太多啦，停下清理御魂吧！")




class SelectedPlace(Ui_start):
    def __init__(self, oldWindows):
        self.Mainwindow = oldWindows
        self.turnTimes = 0

        self.label1 = QLabel("窗口句柄的值为: ", self.Mainwindow)
        self.label2 = QLabel("暂无数据", self.Mainwindow)
        self.label3 = QLabel("进程标题： ", self.Mainwindow)
        self.label4 = QLabel("暂无数据", self.Mainwindow)
        self.label5 = QLabel("窗口的句柄:", self.Mainwindow)
        self.label6 = QLabel("每轮时间(秒):", self.Mainwindow)
        self.label7 = QLabel("当前鼠标位置:",self.Mainwindow)
        self.label8 = QLabel("暂无数据",self.Mainwindow)
        self.label9 = QLabel("开始点击位置(X,Y):",self.Mainwindow)
        self.label10 = QLabel("其他点击的位置(X,Y):",self.Mainwindow)
        self.label11 = QLabel("已经打了:",self.Mainwindow)
        self.label12 = QLabel("0轮",self.Mainwindow)

        self.line1 = QLineEdit(self.Mainwindow)
        self.line1.setMaximumWidth(100)
        self.line2 = QLineEdit(self.Mainwindow)
        self.line2.setMaximumWidth(100)
        self.line3 = QLineEdit(self.Mainwindow)
        self.line3.setMaximumWidth(100)
        self.line3.setPlaceholderText("例如100 200")
        self.line4 = QLineEdit(self.Mainwindow)
        self.line4.setMaximumWidth(100)
        self.line4.setPlaceholderText("例如100 200")

        self.confirm_button = QPushButton('开始', self.Mainwindow)
        self.cancel_button = QPushButton('停止', self.Mainwindow)

        layout1 = QFormLayout() #负责显示左右一对一的
        buttonLayout = QHBoxLayout()
        layoutAll = QVBoxLayout()
        layout1.addRow(self.label1, self.label2)
        layout1.addRow(self.label3, self.label4)
        layout1.addRow(self.label7, self.label8)
        layout1.addRow(self.label5,self.line1)
        layout1.addRow(self.label6, self.line2)
        layout1.addRow(self.label9, self.line3)
        layout1.addRow(self.label10, self.line4)
        layout1.addRow(self.label11, self.label12)

        buttonLayout.addWidget(self.confirm_button)
        buttonLayout.addWidget(self.cancel_button)

        layoutAll.addLayout(layout1)
        layoutAll.addLayout(buttonLayout)

        self.widget = QWidget()
        self.widget.setLayout(layoutAll)
        self.Mainwindow.setCentralWidget(self.widget)

        self.confirm_button.clicked.connect(self.action9_confirm)

        # 改变标签显示句柄用的线程函数
        self.labelChange = threading.Thread(target=lambda: thead_SetHwndLabel(self.label2, self.label4, self.label8))
        self.labelChange.start()
    def action9_confirm(self):
        self.turnTimes = 0

        self.hwnd = self.line1.text()
        self.turnTimeEach = self.line2.text()
        self.begainPos = self.line3.text()
        self.otherPos = self.line4.text()
        if self.hwnd != "" and self.turnTimeEach != "" and self.begainPos != ""and self.otherPos != "":
            bgX,bgY = self.posTransition(self.begainPos)
            otherX,otherY = self.posTransition(self.otherPos)
            try:
                self.bgX = int(bgX)
                self.bgY = int(bgY)
                self.otherX = int(otherX)
                self.otherY = int(otherY)
            except:
                QMessageBox.information(self.Mainwindow, '提示', '请按示例格式输入！')
                return

            self.windows = option.MyWindows(int(self.hwnd))
            if self.windows.checkWindows() == 1:
                QMessageBox.information(self.Mainwindow, '提示', '输入句柄有误！')
                return
            if self.bgX > 1920 or self.bgX < 0 or self.bgY > 1080 or self.bgY < 0 or self.otherX > 1920 or self.otherX < 0 or self.otherY > 1920 or self.otherY < 0:
                QMessageBox.information(self.Mainwindow, '提示', '请输入正确范围的数字！')
                return
            self.windows.random_Wx_select = self.bgX
            self.windows.random_Wy_select = self.bgY
            self.windows.random_Wx_other_select = self.otherX
            self.windows.random_Wy_other_select = self.otherY

            self.clicktread = threading.Thread(target=self.action9_thead_MouseClick)
            self.clicktread.start()

            self.cancel_button.clicked.connect(self.action9_cancel)
            self.confirm_button.clicked.disconnect(self.action9_confirm)
            self.confirm_button.clicked.connect(self.action9_cannotClick)


        else:
            QMessageBox.information(self.Mainwindow, '提示', '请勿输入为空')
            return
    def action9_cancel(self):
        global optionStaus
        optionStaus = 0

        #self.cancel_button.clicked.disconnect()
        #self.confirm_button.clicked.connect(self.action9_confirm)
        #self.confirm_button.clicked.disconnect(self.action9_cannotClick)

        option.stop_thread(self.clicktread)
        QMessageBox.information(self.Mainwindow, '提示', '成功停止！')

    def action9_cannotClick(self):
        QMessageBox.information(self.Mainwindow, '提示', '请先停止当前的点击！')

    def action9_thead_MouseClick(self):
        global optionStaus
        optionStaus = 1

        option.turnOneSelect(self.windows)
        option.WaitTime(1)
        while(1):
            option.selectOne(self.windows, self.turnTimeEach)
            self.turnTimes += 1
            self.label12.setText(str(self.turnTimes) + "轮")

    def posTransition(self,posStr):
        pattern = re.compile(r'-?\d+')
        numStr = pattern.findall(posStr)
        return numStr[0], numStr[1]

# 保持label标签同步线程函数
def thead_SetHwndLabel(label1, label2, label3):
    try:
        oldHwnd = 0
        while(1):
            hwnd = option.GetWindowHwnd()
            X, Y = option.GetMousePosition()
            if oldHwnd != hwnd:
                label1.setText(str(hwnd))
                label2.setText(str(win32gui.GetWindowText(hwnd)))

            if label3 != None:
                label3.setText("({0},{1})".format(X, Y))
            oldHwnd = hwnd
            time.sleep(0.1)
    except:
        pass



