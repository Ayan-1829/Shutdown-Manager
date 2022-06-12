from tkinter import *
from ctypes import windll
from BlurWindow.blurWindow import blur

root = Tk()
root.config(bg='green')
root.wm_attributes("-transparent", 'green')
root.geometry('500x400')

root.update()

hWnd = windll.user32.GetForegroundWindow()
blur(hWnd)


def show(e):
    print("entered")
def show2(e):
    print("left")

root.bind("<Enter>",show)
root.bind("<Leave>",show2)


root.mainloop()