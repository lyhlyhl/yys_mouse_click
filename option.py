import win32api
import win32con
import win32gui
import time
import threading
import random

a=win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
b=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)


class BasicOption:
    def mouse_move(self,x,y):
        win32api.SetCursorPos((x, y))
    def mouse_click(self,x=None,y=None):
        if not x is None and not y is None:
            self.mouse_move(x,y)
            time.sleep(0.005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(random.uniform(0.1, 0.2))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    def get_position(self):
         return win32api.GetCursorPos()

class Option():
    def __init__(self,BasicOption):
        self.BasicOption = BasicOption
    def yuling_single(self):
        time.sleep(1)
        self.BasicOption.mouse_click(860,random.randint(458,478))
        time.sleep(70)
        self.BasicOption.mouse_click(550,random.randint(479,500))
        time.sleep(1)
        self.BasicOption.mouse_click(550, random.randint(479,500))
        time.sleep(1)
        self.BasicOption.mouse_click(550, random.randint(479,500))
        time.sleep(1)
    def yuling_trouble(self):
        time.sleep(5)
        while 1:
            time.sleep(1)
            self.BasicOption.mouse_click(855,random.randint(984,1000))
            time.sleep(80)
            self.BasicOption.mouse_click(random.randint(527,653),999)
            time.sleep(1)
            self.BasicOption.mouse_click(random.randint(527,653),999)
            time.sleep(1)
            self.BasicOption.mouse_click(random.randint(527,653),999)
            time.sleep(1)
Bo=BasicOption()
o = Option(Bo)
o.yuling_trouble()

'''
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









