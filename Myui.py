
import tkinter as tk
import tkinter.messagebox

class MyUiWindow:
    def __init__(self,window):
        self.window = window
    def InitWindow(self):
        self.window.title('痒痒鼠脚本')
        self.window.geometry('400x300')
        self.window.iconbitmap("bitbug_favicon.ico")
        menubar = tk.Menu(self.window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu1 = tk.Menu(menubar, tearoff=0)
        filemenu2 = tk.Menu(menubar, tearoff=0)


        menubar.add_cascade(label='模式', menu=filemenu)
        menubar.add_cascade(label='说明', menu=filemenu1)
        menubar.add_cascade(label='关于', menu=filemenu2)

        submenu = tk.Menu(filemenu)

        filemenu.add_cascade(label='御魂', menu=submenu)
        submenu.add_command(label='单人', command=self.hit_me)
        submenu.add_command(label='双人', command=self.hit_me)
        submenu.add_command(label='三人', command=self.hit_me)

        filemenu.add_command(label='御灵', command=self.hit_me)
        filemenu.add_command(label='贪痴念', command=self.hit_me)


        self.window.config(menu=menubar)
       # window.maxsize(width=200, height=300)
    # window.minsize(width=200, height=300
    def hit_me(self):
        tkinter.messagebox.showinfo(title='警告', message='test')