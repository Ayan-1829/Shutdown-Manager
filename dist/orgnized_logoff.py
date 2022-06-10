import os
import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import subprocess


class topWindow():

    def __init__(self):
        self.pu = tkinter.Toplevel(st)
        self.pu.config(bg='#dddddd')
        # self.pu.geometry('540x180')
        self.hour = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                     '18',
                     '19', '20', '21', '22', '23']
        self.min = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                    '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                    '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

        # self.var1 = self.StringVar()
        # self.var2 = self.StringVar()
        # self.var3 = self.StringVar()
        # self.var4 = self.StringVar()

        label_fnt = ('Times', 15, 'bold')
        label_background = '#cccccc'

        ########### time after ###########
        self.l1 = tkinter.Label(self.pu, font=label_fnt, bg=label_background, fg='white')
        self.l1.grid(row=0, column=0, padx=10, pady=10)

        self.cmb1 = ttk.Combobox(self.pu, value=self.hour, width=10)
        self.cmb1.grid(row=0, column=1, padx=1, pady=10)

        self.l2 = tkinter.Label(self.pu, text='Hours', font=label_fnt, bg=label_background, fg='white')
        self.l2.grid(row=0, column=2, padx=10, pady=10)

        self.cmb2 = ttk.Combobox(self.pu, value=self.min, width=10)
        self.cmb2.grid(row=0, column=3, padx=1, pady=10)

        self.l3 = tkinter.Label(self.pu, text='Mins', font=label_fnt, bg=label_background, fg='white')
        self.l3.grid(row=0, column=4, padx=10, pady=10)

        self.button1 = tkinter.Button(master=self.pu, text='save', bg='#aabbff', font=('Times New Roman', 15, 'bold'),
                                      width=6)
        self.button1.grid(row=0, column=5, padx=10, pady=10)

        ############ time at ##########
        self.l4 = tkinter.Label(self.pu, font=label_fnt, bg=label_background, fg='white')
        self.l4.grid(row=1, column=0, padx=10, pady=10)

        self.cmb3 = ttk.Combobox(self.pu, value=self.hour, width=10)
        self.cmb3.grid(row=1, column=1, padx=1, pady=10)

        self.l5 = tkinter.Label(self.pu, text='Hours', font=label_fnt, bg=label_background, fg='white')
        self.l5.grid(row=1, column=2, padx=10, pady=10)

        self.cmb4 = ttk.Combobox(self.pu, value=self.min, width=10)
        self.cmb4.grid(row=1, column=3, padx=1, pady=10)

        self.l6 = tkinter.Label(self.pu, text='Mins', font=label_fnt, bg=label_background, fg='white')
        self.l6.grid(row=1, column=4, padx=10, pady=10)

        self.button2 = tkinter.Button(master=self.pu, text='save', bg='#aabbff', font=label_fnt,
                                      width=6)
        self.button2.grid(row=1, column=5, padx=10, pady=10)

        ########### Close button ##########
        self.now_button = tkinter.Button(master=self.pu,
                                         text="Now",
                                         # text_color='White',
                                         # border_width=3,
                                         # border_color='white',
                                         # corner_radius=15,
                                         bg='#aabbff',
                                         fg='black',
                                         font=label_fnt,

                                         width=6
                                         )
        self.now_button.grid(row=2, column=1, pady=3)
        self.close_button = tkinter.Button(master=self.pu,
                                           text="Cancel",
                                           # text_color='White',
                                           # border_width=3,
                                           # border_color='white',
                                           # corner_radius=15,
                                           bg='red',
                                           fg='white',
                                           font=label_fnt,
                                           command=self.pu.destroy,
                                           width=6
                                           )
        self.close_button.grid(row=2, column=3, pady=3)


def cal_after(a, b):
    return (a * 60 + b) * 60


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

    obj = topWindow()

    obj.button1.config(command=f_after)
    obj.button2.config(command=f_at)
    obj.now_button.config(command=f_now)

    obj.l1.config(text='Shutdown after:')
    obj.l4.config(text='Shutdown at:')

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

def restart():
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

    obj = topWindow()

    obj.button1.config(command=f_after)
    obj.button2.config(command=f_at)
    obj.now_button.config(command=f_now)

    obj.l1.config(text='Shutdown after:')
    obj.l4.config(text='Shutdown at:')

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

def lock():
    os.system('shutdown -l')

def hybernate():
    os.system('shutdown -h')

def abort():
    os.system("shutdown -a")


st = tkinter.Tk()
st.attributes('-transparentcolor', '#012345')
st.title("Task Scheduler")
st.geometry("400x540")
st.config(bg='#012345')
# st.overrideredirect(True)

x_coordinate = 100
y_coordinate = 60

button_font = ('Times', 15, 'bold')
button_width = 160
button_hight = 40
button_distance = 45

# r_button = customtkinter.CTkButton(master=st,
#                                    text="Restart",
#                                    text_color='white',
#                                    border_width=3,
#                                    border_color='white',
#                                    corner_radius=15,
#                                    text_font=('Times New Roman', 25),
#                                    command=restart
#                                    )
# r_button.place(x=100, y=60, width=200, height=50)

shutdown_button = tkinter.Button(master=st,
                          text="Restart",
                          # text_color='white',
                          # border_width=3,
                          # border_color='white',
                          # corner_radius=15,
                          # text_font=('Times New Roman', 25),
                          bg='#12ffdd',
                          font=button_font,
                          command=lambda: restart()
                          )
shutdown_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance

restart_button = tkinter.Button(master=st,
                                   text="Shutdown",
                                   # text_color='white',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=button_font,
                                   command=shutdown
                                   )
restart_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance

lock_button = tkinter.Button(master=st,
                                   text="Lock",
                                   # text_color='white',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=button_font,
                                   command=lock
                                   )
lock_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance

hybernate_button = tkinter.Button(master=st,
                                   text="Hybernate",
                                   # text_color='white',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=button_font,
                                   command=hybernate
                                   )
hybernate_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance

scroff_button = tkinter.Button(master=st,
                                   text="Screen off",
                                   # text_color='white',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=button_font,
                                   command=screen_off
                                   )
scroff_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance

abort_button = tkinter.Button(     master=st,
                                   text="Abort",
                                   # text_color='White',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=button_font,
                                   command=abort
                                   )
abort_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance

r_button = tkinter.Button(master=st,
                                   text="Close",
                                   # text_color='White',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='red',
                                   fg='white',
                                   font=('Times', 20, 'bold'),
                                   command=st.destroy
                                   )
r_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
y_coordinate += button_distance


# os.startfile("C:\Others\Studies\Mid_Night_Thoughts\mynotepad\mynotepad.exe")

st.mainloop()

