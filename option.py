import win32api
import win32con
import win32gui
import time
import threading
import random

a=win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
b=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

def MouseMove(x,y):     #移动鼠标的位置
    win32api.SetCursorPos((x, y))
def MouseClick(x=None,y=None):  #鼠标点击指定的地方
    if not x is None and not y is None:
        MouseMove(x,y)
        time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(random.uniform(0.001, 0.02))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def GetMousePosition():     #得到鼠标的位置
     return win32api.GetCursorPos()

class MyWindows:    #新建一个窗口类
    def __init__(self):
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.hwnd = None
        self.random_x_fight = random.uniform(0.92,0.97)
        self.random_y_fight = random.uniform(0.84, 0.92)
    def GetWindowsHwnd(self):   #得到鼠标对应位置的应用句柄
        X,Y=GetMousePosition()
        hwnd = win32gui.WindowFromPoint((X, Y))
        self.hwnd = hwnd
        return hwnd
    def GetWindowsPostion(self):    #可以直接得到鼠标对应窗口的位置
        return win32gui.GetWindowRect(self.GetWindowsHwnd())
    def GetWindowsRect(self):
        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(self.hwnd)
    def ChangeWindows(self,left,top,width,hight):   #改变窗口的位置
        win32gui.MoveWindow(self.hwnd, left, top, width, hight, True)
    def WindowsMoveClick(self, random_x,random_y):
        MouseClick(int((self.right-self.left)*random_x)+20,int((self.bottom-self.top)*random_y)+20)

wd= MyWindows()
while(1):
    #if():
    if (win32api.GetAsyncKeyState(0x20)&0x8000 != 0) :
        print(wd.GetWindowsHwnd())
        wd.ChangeWindows(20,20,500,500)
        wd.GetWindowsRect()
        print(int((wd.right-wd.left)*wd.random_x_fight))
        while(1):
           if win32api.GetAsyncKeyState(0x20) == 0 :
               wd.WindowsMoveClick(wd.random_x_fight, wd.random_y_fight)
               break

    #print((win32api.GetAsyncKeyState(0x41)&0x8000))
    '''
    print(wd.GetWindowsHwnd())
    win32gui.SetForegroundWindow(wd.GetWindowsHwnd());
    print(wd.GetWindowsPostion())
    wd.DrawWindowsRect()
    time.sleep(0.5)
    '''

'''
def yuling_single():
    time.sleep(1)
    mouse_click(860,random.randint(458,478))
    time.sleep(70)
    mouse_click(550,random.randint(479,500))
    time.sleep(1)
    mouse_click(550, random.randint(479,500))
    time.sleep(1)
    mouse_click(550, random.randint(479,500))
    time.sleep(1)
def yuling_trouble():
    time.sleep(5)
    while 1:
        time.sleep(1)
        mouse_click(855,random.randint(984,1000))
        time.sleep(80)
        mouse_click(random.randint(527,653),999)
        time.sleep(1)
        mouse_click(random.randint(527,653),999)
        time.sleep(1)
        mouse_click(random.randint(527,653),999)
        time.sleep(1)


def yuling3():
    time.sleep(45)
    while 1:
        time.sleep(1)
        mouse_click(1729,random.randint(957,985))
        time.sleep(85)
        mouse_click(random.randint(1427,1553),979)
        time.sleep(1)
        mouse_click(random.randint(1427,1553),979)
        time.sleep(1)
        mouse_click(random.randint(1427,1553),979)
        time.sleep(1)
def turn_three():
    mouse_click(550, random.randint(400, 450))
    time.sleep(random.uniform(0.1, 0.5))
    mouse_click(random.randint(527, 653), 999)
    time.sleep(random.uniform(0.1, 0.5))
    mouse_click(random.randint(1427, 1553), 979)
    time.sleep(random.uniform(0.1, 0.5))
def three_snake_11():
    while 1:
        mouse_click(1729, random.randint(957, 985))
        time.sleep(80)
        turn_three()
        time.sleep(1)
        turn_three()
        time.sleep(1)
        turn_three()
        time.sleep(1)
        turn_three()
        time.sleep(3)

def turn_two():
    mouse_click(random.randint(400, 450),400)
    time.sleep(random.uniform(0.1, 0.5))
    mouse_click(random.randint(527, 653), 930)
    time.sleep(random.uniform(0.1, 0.5))
def two_snake_11():
    while 1:
        turn_two()
        time.sleep(3)
        mouse_click( random.randint(879, 889),random.randint(445, 456))
        time.sleep(50)
        turn_two()
        time.sleep(1)
        turn_two()
        time.sleep(1)
        turn_two()
        time.sleep(1)



#mouse_click(1729, random.randint(957, 985))
#yuling1()
#yuling1()
#get_position()
#yuling()
#print(s)
#three_snake_11()
#two_snake_11()

print(x)
print(y)
mouse_move(331,818)
while 1:
    mouse_click(331, 798)
    time.sleep(3)
    print(1)



# 每隔10秒钟执行
def t2():
    yuling1()
if __name__ == '__main__':
    t = threading.Thread(target=t2)
   # v = threading.Thread(target=yuling3)
    t.start()
    #v.start()
    yuling2()
    t.join()
    #v.join()
'''


#BO = BasicOption
#BO.mouse_click(855,random.randint(984,1000))



'''

class GetWindows():
    def __init__(self):
        self.spying = False

    def mouseMoveEvent(self):
        curX, curY = win32gui.GetCursorPos()
        hwnd = win32gui.WindowFromPoint((curX, curY))
        print(hwnd)
        time.sleep(0.2)


#wind = GetWindows()
#while(1):
#    wind.mouseMoveEvent()


'''









