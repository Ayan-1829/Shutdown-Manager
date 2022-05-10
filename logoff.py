import os
import tkinter
from tkinter import *
import tkinter.messagebox
# import customtkinter
from tkinter import ttk
import time


# from popUp import *

# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")


# def pop_up():
#     pass


def restart():
    # pu = customtkinter.CTkToplevel(st)
    pu = tkinter.Toplevel(st)
    pu.attributes('-transparentcolor', '#012345')
    pu.geometry('450x180')
    pu.config(bg='#012345')

    def f_now():
        pu.destroy()
        pu.quit()
        os.system("shutdown -r -t 2")

    def f_restart():
        a = int(var1.get())
        b = int(var2.get())
        work = (a * 60 + b) * 60
        pu.destroy()
        # print(work)
        os.system(f"shutdown -r -t {work}")

    def f_shutdown():
        a = int(var3.get())
        b = int(var4.get())

        ctime = time.localtime(time.time())
        hour = ctime.tm_hour
        minute = ctime.tm_min
        second = ctime.tm_sec

        # print(str(a) + ' ' + str(hour))

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

        # print(str(a) + ' ' + str(b) + ' ' + str(c))

        work = (a * 60 + b) * 60 + c
        pu.destroy()
        os.system(f"shutdown -r -t {work}")

    hour = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23']
    min = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    ########### At time ###########
    l1 = tkinter.Label(pu, text='Restart after:', font=('Times', 12, 'bold'), bg="#012345", fg='white')
    l1.grid(row=0, column=0, padx=10, pady=10)

    cmb1 = ttk.Combobox(pu, value=hour, textvariable=var1, width=10)
    cmb1.grid(row=0, column=1, padx=10, pady=10)
    cmb1.current(0)

    cmb2 = ttk.Combobox(pu, value=min, textvariable=var2, width=10)
    cmb2.grid(row=0, column=2, padx=10, pady=10)
    cmb2.current(0)

    button = tkinter.Button(master=pu, text='save', bg='#aabbff', font=('Times New Roman', 15, 'bold'), command=f_restart, width=6)
    button.grid(row=0, column=3, padx=10, pady=10)

    ############ From Now ##########
    l1 = tkinter.Label(pu, text='Restart At:', font=('Times', 12, 'bold'), bg="#012345", fg='white')
    l1.grid(row=1, column=0, padx=10, pady=10)

    cmb3 = ttk.Combobox(pu, value=hour, textvariable=var3, width=10)
    cmb3.grid(row=1, column=1, padx=10, pady=10)
    cmb3.current(0)

    cmb4 = ttk.Combobox(pu, value=min, textvariable=var4, width=10 )
    cmb4.grid(row=1, column=2, padx=10, pady=10)
    cmb4.current(0)

    button = tkinter.Button(master=pu, text='save', bg='#aabbff', font=('Times New Roman', 15, 'bold'), command=f_shutdown, width=6)
    button.grid(row=1, column=3, pady=10, padx=10)

    ########### Close button ##########
    close_button = tkinter.Button(master=pu,
                                  text="Now",
                                  # text_color='White',
                                  # border_width=3,
                                  # border_color='white',
                                  # corner_radius=15,
                                  bg='#aabbff',
                                  fg='black',
                                  font=('Times', 15, 'bold'),
                                  command=f_now,
                                  width=6
                                  )
    close_button.grid(row=2, column=1, pady=3)
    close_button = tkinter.Button(master=pu,
                                  text="Cancel",
                                  # text_color='White',
                                  # border_width=3,
                                  # border_color='white',
                                  # corner_radius=15,
                                  bg='red',
                                  fg='white',
                                  font=('Times', 15, 'bold'),
                                  command=pu.destroy,
                                  width=6
                                  )
    close_button.grid(row=2, column=2, pady=3)

    pu.mainloop()
    # print('restart_time')


def shutdown():
    pu = tkinter.Toplevel(st)
    pu.attributes('-transparentcolor', '#012345')
    pu.geometry('450x180')
    pu.config(bg='#012345')

    def f_now():
        pu.destroy()
        os.system('shutdown -s -t 2')

    def f_restart():
        a = int(var1.get())
        b = int(var2.get())
        work = (a * 60 + b) * 60
        pu.destroy()
        # print(work)
        os.system(f"shutdown -s -t {work}")

    def f_shutdown():
        a = int(var3.get())
        b = int(var4.get())

        ctime = time.localtime(time.time())
        hour = ctime.tm_hour
        minute = ctime.tm_min
        second = ctime.tm_sec

        # print(str(a) + ' ' + str(hour))

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

        # print(str(a) + ' ' + str(b) + ' ' + str(c))

        work = (a * 60 + b) * 60 + c
        pu.destroy()
        os.system(f"shutdown -s -t {work}")

    hour = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23']
    min = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    ########### At time ###########
    l1 = tkinter.Label(pu, text='Shutdown after:', font=('Times', 12, 'bold'), bg="#012345", fg='white')
    l1.grid(row=0, column=0, padx=10, pady=10)

    cmb1 = ttk.Combobox(pu, value=hour, textvariable=var1, width=10)
    cmb1.grid(row=0, column=1, padx=10, pady=10)
    cmb1.current(0)

    cmb2 = ttk.Combobox(pu, value=min, textvariable=var2, width=10)
    cmb2.grid(row=0, column=2, padx=10, pady=10)
    cmb2.current(0)

    button = tkinter.Button(master=pu, text='save', bg='#aabbff', font=('Times New Roman', 15, 'bold'),
                            command=f_restart, width=6)
    button.grid(row=0, column=3, padx=10, pady=10)

    ############ From Now ##########
    l1 = tkinter.Label(pu, text='Shutdown At:', font=('Times', 12, 'bold'), bg="#012345", fg='white')
    l1.grid(row=1, column=0, padx=10, pady=10)

    cmb3 = ttk.Combobox(pu, value=hour, textvariable=var3, width=10)
    cmb3.grid(row=1, column=1, padx=10, pady=10)
    cmb3.current(0)

    cmb4 = ttk.Combobox(pu, value=min, textvariable=var4, width=10)
    cmb4.grid(row=1, column=2, padx=10, pady=10)
    cmb4.current(0)

    button = tkinter.Button(master=pu, text='save', bg='#aabbff', font=('Times New Roman', 15, 'bold'),
                            command=f_shutdown, width=6)
    button.grid(row=1, column=3, pady=10, padx=10)

    ########### Close button ##########
    close_button = tkinter.Button(master=pu,
                                  text="Now",
                                  # text_color='White',
                                  # border_width=3,
                                  # border_color='white',
                                  # corner_radius=15,
                                  bg='#aabbff',
                                  fg='black',
                                  font=('Times', 15, 'bold'),
                                  command=f_now,
                                  width=6
                                  )
    close_button.grid(row=2, column=1, pady=3)
    close_button = tkinter.Button(master=pu,
                                  text="Cancel",
                                  # text_color='White',
                                  # border_width=3,
                                  # border_color='white',
                                  # corner_radius=15,
                                  bg='red',
                                  fg='white',
                                  font=('Times', 15, 'bold'),
                                  command=pu.destroy,
                                  width=6
                                  )
    close_button.grid(row=2, column=2, pady=3)

    pu.mainloop()
    # os.system("shutdown -s -t 5")
    # print('shutdown')


def abort():
    os.system("shutdown -a")
    # print('abort')


st = tkinter.Tk()
st.attributes('-transparentcolor', '#012345')
st.title("Task Scheduler")
st.geometry("400x360")
st.config(bg='#012345')
# st.overrideredirect(True)

x_coordinate = 100
y_coordinate = 60

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

r_button = tkinter.Button(master=st,
                          text="Restart",
                          # text_color='white',
                          # border_width=3,
                          # border_color='white',
                          # corner_radius=15,
                          # text_font=('Times New Roman', 25),
                          bg='#12ffdd',
                          font=('Times', 20, 'bold'),
                          command=lambda: restart()
                          )
r_button.place(x=100, y=120 - 60, width=200, height=50)

r_button = tkinter.Button(master=st,
                                   text="Shutdown",
                                   # text_color='white',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=('Times', 20, 'bold'),
                                   command=shutdown
                                   )
r_button.place(x=100, y=180 - 60, width=200, height=50)

r_button = tkinter.Button(         master=st,
                                   text="Abort",
                                   # text_color='White',
                                   # border_width=3,
                                   # border_color='white',
                                   # corner_radius=15,
                                   # text_font=('Times New Roman', 25),
                                   bg='#12ffdd',
                                   font=('Times', 20, 'bold'),
                                   command=abort
                                   )
r_button.place(x=100, y=240 - 60, width=200, height=50)

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
r_button.place(x=100, y=300 - 60, width=200, height=50)


# os.startfile("C:\Others\Studies\Mid_Night_Thoughts\mynotepad\mynotepad.exe")

st.mainloop()
