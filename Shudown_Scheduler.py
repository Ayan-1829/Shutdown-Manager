import os
import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import subprocess
import psutil

from ctypes import windll

# from BlurWindow.blurWindow import blur

class topWindow:

    def __init__(self):
        self.pu = tkinter.Toplevel(st)
        self.pu.attributes('-transparentcolor', '#223333')
        self.pu.config(bg='#abefef')
        self.pu.resizable(False,False)

        self.sand_box = PhotoImage(file='icon/hourglass.png')
        self.sand_box = self.sand_box.subsample(12)

        self.clock = PhotoImage(file='icon/clock.png')
        self.clock = self.clock.subsample(12)

        # self.pu.geometry('600x270')
        self.hour = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        self.min = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                    '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                    '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

        label_fnt = ('Times', 14, 'bold')
        label_background = '#abefef'
        label_foreground = '#012323'

        row = 0
        col = 0

        button_font = ('Times', 12, 'bold')

        self.heading = tkinter.Label(self.pu, bg=label_background, fg=label_foreground, font=('Roboto',20, 'underline', 'bold'))
        self.heading.grid(row=row, column=col, columnspan=7, pady=10)

        # ----------- time after -------------
        row += 1
        self.l0 = tkinter.Label(self.pu, bg=label_background, image=self.sand_box,  compound=LEFT)
        self.l0.grid(row=row, column=col, pady=0, padx=10)
        col += 1
        self.l1 = tkinter.Label(self.pu, font=label_fnt, bg=label_foreground, fg=label_background)
        self.l1.grid(row=row, column=col)
        col += 1

        self.cmb1 = ttk.Combobox(self.pu, value=self.hour, width=4)
        self.cmb1.grid(row=row, column=col)
        col += 1

        self.l2 = tkinter.Label(self.pu, text='Hours', font=label_fnt, bg=label_background, fg=label_foreground)
        self.l2.grid(row=row, column=col)
        col += 1

        self.cmb2 = ttk.Combobox(self.pu, value=self.min, width=4)
        self.cmb2.grid(row=row, column=col)
        col += 1

        self.l3 = tkinter.Label(self.pu, text='Minutes', font=label_fnt, bg=label_background, fg=label_foreground)
        self.l3.grid(row=row, column=col)
        col += 1

        self.button1 = tkinter.Button(master=self.pu, text='save', bg='#12ffdd', font=button_font,
                                      border=5, width=6, cursor='hand2',
                                      )
        self.button1.grid(row=row, column=col,padx=15, pady=10)
        col += 1
        self.button1.bind("<Enter>", lambda x: self.button1.config(bg='#018888', fg='white'))
        self.button1.bind("<Leave>", lambda x: self.button1.config(bg='#12ffdd', fg='black'))

        # ----------- time at ---------------
        row +=1
        col = 0
        self.l0 = tkinter.Label(self.pu, bg=label_background, image=self.clock, compound=LEFT)
        self.l0.grid(row=row, column=col)
        col += 1
        self.l4 = tkinter.Label(self.pu, font=label_fnt, bg=label_foreground, fg=label_background)
        self.l4.grid(row=row, column=col)
        col += 1

        self.cmb3 = ttk.Combobox(self.pu, value=self.hour, width=4)
        self.cmb3.grid(row=row, column=col)
        col += 1

        self.l5 = tkinter.Label(self.pu, text='Hours', font=label_fnt, bg=label_background, fg=label_foreground)
        self.l5.grid(row=row, column=col)
        col += 1

        self.cmb4 = ttk.Combobox(self.pu, value=self.min, width=4)
        self.cmb4.grid(row=row, column=col)
        col += 1

        self.l6 = tkinter.Label(self.pu, text='Minutes', font=label_fnt, bg=label_background, fg=label_foreground)
        self.l6.grid(row=row, column=col)
        col += 1

        self.button2 = tkinter.Button(master=self.pu, text='save', bg='#12ffdd', font=button_font,
                                      border=5, width=6)
        self.button2.grid(row=row, column=col,padx=7, pady=5)
        self.button2.bind("<Enter>", lambda x: self.button2.config(bg='#018888', fg='white'))
        self.button2.bind("<Leave>", lambda x: self.button2.config(bg='#12ffdd', fg='black'))

        # ---------- Close button ------------
        row = 4
        col = 2
        self.now_button = tkinter.Button(master=self.pu,
                                         text="Now",
                                         # text_color='White',
                                         # border_width=3,
                                         # border_color='white',
                                         # corner_radius=15,
                                         bg='#12ffdd',
                                         fg='black',
                                         font=button_font,
                                         border=5,
                                         width=6
                                         )
        self.now_button.grid(row=row, column=col, pady=15)
        col += 2
        self.now_button.bind("<Enter>", lambda x: self.now_button.config(bg='#018888',fg='white'))
        self.now_button.bind("<Leave>", lambda x: self.now_button.config(bg='#12ffdd', fg='black'))
        self.close_button = tkinter.Button(master=self.pu,
                                           text="Cancel",
                                           bg='red',
                                           fg='white',
                                           font=button_font,
                                           border=5,
                                           command=self.pu.destroy,
                                           width=6
                                           )
        self.close_button.grid(row=row, column=col, pady=15)
        self.close_button.bind("<Enter>", lambda x: self.close_button.config(bg='#990000'))
        self.close_button.bind("<Leave>", lambda x: self.close_button.config(bg='red'))

# Calculation for Shutdownn after
def cal_after(a, b):
    return (a * 60 + b) * 60

# Calculation for Shutdownn at
def cal_at(a, b):
    ctime = time.localtime(time.time())
    hour = ctime.tm_hour
    minute = ctime.tm_min
    second = ctime.tm_sec

    if a < hour:
        a += 24
    a = a - hour

    if b < minute:
        a -= 1
        b += 60
    b = b - minute

    c = 0
    if c < second:
        b -= 1
        c += 60
    c = c - second

    return (a * 60 + b) * 60 + c


def shutdown():
    obj = topWindow()
    # obj.pu.geometry('630x265')
    obj.pu.title("Shutdown menu")
    obj.heading.config(text="SHUTDOWN  MENU")

    def f_now():
        os.system('shutdown -s -t 1')

    def f_after():
        a = int(v1.get())
        b = int(v2.get())
        work = cal_after(a, b)
        obj.pu.destroy()
        # print(work)
        os.system(f"shutdown -s -t {work}")

    def f_at():
        a = int(v3.get())
        b = int(v4.get())
        work = cal_at(a, b)
        obj.pu.destroy()
        os.system(f"shutdown -s -t {work}")

    def process_idle():
        obj.pu.destroy()
        st.destroy()
        p = psutil.Process(0)
        count = 0
        while True:
            cpu = p.cpu_percent(interval=1) / psutil.cpu_count()

            t = int(value.get()) * 60

            if cpu > 85:
                count += 1
            else:
                count = 0

            # print("CPU percentage   : ", "{:.25f}".format(cpu))
            # print(count)
            # print()

            if count >= t:
                # print("*****************************************************")
                # print(f"Idle for {count} seconds")
                os.system("shutdown -s -t 1")

    # --------- Process idle -------------

    label_fnt = ('Times', 14, 'bold')
    label_background = '#abefef'
    label_foreground = '#012323'

    sleeping = PhotoImage(file='icon/sleeping.png')
    sleeping = sleeping.subsample(10)

    row = 3
    col = 0
    obj.time = ['1', '2', '3', '4', '5', '10', '11', '15', '20', '25', '30']

    l0 = tkinter.Label(obj.pu, bg=label_background, image=sleeping,)
    l0.grid(row=row, column=col)
    col += 1
    obj.l7 = tkinter.Label(obj.pu, text='          CPU Process Idle for :          ', font=label_fnt,
                           bg=label_foreground, fg=label_background)
    obj.l7.grid(row=row, column=col, columnspan=3)
    col += 3

    obj.cmb5 = ttk.Combobox(obj.pu, value=obj.time, width=4)
    obj.cmb5.grid(row=row, column=col)
    obj.cmb5.current(4)
    col += 1

    obj.l7 = tkinter.Label(obj.pu, text='Minutes', font=label_fnt, bg=label_background, fg=label_foreground)
    obj.l7.grid(row=row, column=col)
    col += 1

    obj.button3 = tkinter.Button(master=obj.pu, text='save', bg='#12ffdd', font=('Times', 12, 'bold'), border=5, width=6)
    obj.button3.grid(row=row, column=col, pady=10)
    obj.button3.bind("<Enter>", lambda x: obj.button3.config(bg='#018888', fg='white'))
    obj.button3.bind("<Leave>", lambda x: obj.button3.config(bg='#12ffdd', fg='black'))

    obj.button1.config(command=f_after)
    obj.button2.config(command=f_at)
    obj.button3.config(command=process_idle)
    obj.now_button.config(command=f_now)

    obj.l1.config(text='  Shutdown after :  ')
    obj.l4.config(text='    Shutdown at :    ')

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    value = StringVar()
    obj.cmb1.config(textvariable=v1)
    obj.cmb2.config(textvariable=v2)
    obj.cmb3.config(textvariable=v3)
    obj.cmb4.config(textvariable=v4)
    obj.cmb5.config(textvariable=value)

    obj.cmb1.current(0)
    obj.cmb2.current(0)
    obj.cmb3.current(0)
    obj.cmb4.current(0)
    obj.cmb5.current(4)

    obj.pu.mainloop()


def restart():
    obj = topWindow()
    # obj.pu.geometry('605x200')
    obj.pu.title("Restart menu")
    obj.heading.config(text="RESTART  MENU")
    
    def f_now():
        os.system('shutdown -r -t 1')

    def f_after():
        a = int(v1.get())
        b = int(v2.get())
        work = cal_after(a, b)
        obj.pu.destroy()
        # print(work)
        os.system(f"shutdown -r -t {work}")

    def f_at():
        a = int(v3.get())
        b = int(v4.get())
        work = cal_at(a, b)
        obj.pu.destroy()
        os.system(f"shutdown -r -t {work}")

    obj.button1.config(command=f_after)
    obj.button2.config(command=f_at)
    obj.now_button.config(command=f_now)

    obj.l1.config(text='  Restart after :  ')
    obj.l4.config(text='   Restart at :    ')

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    obj.cmb1.config(textvariable=v1)
    obj.cmb2.config(textvariable=v2)
    obj.cmb3.config(textvariable=v3)
    obj.cmb4.config(textvariable=v4)

    obj.cmb1.current(0)
    obj.cmb2.current(0)
    obj.cmb3.current(0)
    obj.cmb4.current(0)

    obj.pu.mainloop()


def screen_off():
    subprocess.call([r'monitor_off.bat'])


def logoff():
    os.system('shutdown -l')


def hibernate():
    os.system('shutdown -h')


def abort():
    os.system("shutdown -a")


st = tkinter.Tk()
st.attributes('-transparentcolor', '#012345')
st.title("Shutdown Scheduler")
st.geometry("320x400")
st.config(bg='#abefef')
# st.config(bg='#012345')
st.iconbitmap(r'icon/shutdown.ico')
st.resizable(False, False)
# st.overrideredirect(True)

# hWnd = windll.user32.GetForegroundWindow()
# blur(hWnd)


def create_main_button(text, command, y_coordinate, bg="#12ffdd"):
    """Creates and places a main window button"""
    f = "black"
    e_bg = "#018888"
    if bg!="#12ffdd":
        f = "#fff"
        e_bg = "#990000"
    button = tkinter.Button(master=st, text=text, border=5, bg=bg, fg=f,  font=('Times', 15, 'bold'), command=command)
    button.place(x=80, y=y_coordinate, width=160, height=40)
    button.bind("<Enter>", lambda x: button.config(bg=e_bg, fg="white"))
    button.bind("<Leave>", lambda x: button.config(bg=bg, fg=f))
    return button

# Create buttons dynamically
buttons = [
    ("Restart", restart),
    ("Shutdown", shutdown),
    ("Sign out", logoff),
    ("Hibernate", hibernate),
    ("Screen off", screen_off),
    ("Abort", abort),
    ("Close", st.destroy, "#ee0000")
]

y = 40
for text, command, *color in buttons:
    create_main_button(text, command, y, *(color if color else []))
    y += 45


# os.startfile("C:\Others\Studies\Mid_Night_Thoughts\mynotepad\mynotepad.exe")

st.mainloop()

