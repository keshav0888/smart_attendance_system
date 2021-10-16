from tkinter import messagebox
import datetime
import time
from tkinter import *
import threading
import pyttsx3
import tkinter as tk
from tkinter import ttk
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Keshav@888",
  database="mydatabase",
  auth_plugin='mysql_native_password'
)
class Timetable(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        select_day= tk.StringVar(self)
        select_branch= tk.StringVar(self)
        select_time1 = tk.StringVar(self)
        select_time2 = tk.StringVar(self)
        select_batch = tk.StringVar(self)
        select_day.set("Select Day")
        select_branch.set("Select Branch")
        select_time1.set("Select Time From")
        select_time2.set("To Time")
        select_batch.set("Select Batch")
        t = threading.Thread(target=self.my_message, args=('Wellcome..',))
        t.start()

        self.title("Timetable Regitration Page In Student Attendanced System")
        self.Top1 = Frame(self, height=1200, bg='#C0C0C0')
        self.Top1.pack(fill=X)


        self.text_lable = Label(self.Top1, text="Time Table", font='arial 19 bold', fg="red", width=30,bg='#C0C0C0')
        self.text_lable.place(x=200, y=30)


        self.lock1 = Label(self.Top1, font='arial 19 bold', fg="RED", bg='#C0C0C0')
        self.lock1.place(x=650, y=20)


        self.day_label=Label(self.Top1,text="Select Day",font='arial 15',fg="green",width=20 )
        self.day_label.place(x=100,y=100)

        self.combox_day = ttk.Combobox(self.Top1, width=20, state='readonly',textvariable = select_day)
        self.combox_day['values'] = ('Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday')
        self.combox_day.place(x=380,y=100)

        self.Time_label = Label(self.Top1, text="Select Time", font='arial 15', fg="green", width=20)
        self.Time_label.place(x=100, y=180)
        self.combox1_time = ttk.Combobox(self.Top1, width=20, state='readonly',textvariable = select_time1)
        self.combox1_time['values'] = ('10:30','11:30','12:30','1:15','2:15','3:15','3:30','4:30')
        self.combox1_time.place(x=380,y=180)

        self.combox2_time = ttk.Combobox(self.Top1, width=20, state='readonly', textvariable=select_time2)
        self.combox2_time['values'] = ('11:30','12:30','1:15','2:15','3:15','3:30','4:30','5:30')
        self.combox2_time.place(x=580, y=180)

        self.sub_label = Label(self.Top1, text="Enter Subject Name", font='arial 15', fg="green", width=20)
        self.sub_label.place(x=100, y=260)
        self.sub_entry=Entry(self.Top1)
        self.sub_entry.place(x=380,y=260)

        self.branch_label = Label(self.Top1, text="Select Branch", font='arial 15', fg="green", width=20)
        self.branch_label.place(x=100, y=340)
        self.combox_sub = ttk.Combobox(self.Top1, width=25, state='readonly',textvariable = select_branch)
        self.combox_sub['values'] = ('Computer Science And Technolgy', 'Chemical Technology', 'Electronic And Communication Technology', 'Food Technology', 'Civil Engineering', 'Mechanical Engineering')
        self.combox_sub.place(x=380, y=340)



        self.batch_label = Label(self.Top1, text="Select Batch", font='arial 15', fg="green", width=20)
        self.batch_label.place(x=100, y=420)
        self.combox_batch = ttk.Combobox(self.Top1, width=25, state='readonly',textvariable = select_batch)
        self.combox_batch['values'] = ('All Batch','B1','B2','B3','B4')
        self.combox_batch.place(x=380, y=420)

        self.SUBMIT_Button = Button(self.Top1, text="SUBMIT", font='arial 15 bold', width=40, bg='green',command=lambda:self.submit())
        self.SUBMIT_Button.place(x=180, y=570)

        def tick1():
            time2 = time.strftime('%H:%M:%S')
            self.lock1.config(text=time2)
            self.lock1.after(200, tick1)

        tick1()

        self.geometry('800x650+350+50')
        self.mainloop()

    def my_message(self, my_message):
        try:

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
            # rate = engine.getProperty('rate')
        except:
            print('Faield to execute my_message function ! ')

    def submit(self):
                day=self.combox_day.get()
                time1=self.combox1_time.get()
                time2= self.combox2_time.get()
                sub=self.sub_entry.get()
                branch=self.combox_sub.get()
                batch=self.combox_batch.get()



                if day != "Select Day" and time != "Select Time" and sub != "" and branch != "Select Branch" and batch!="Select Batch":
                    if time1 != time2 and time2 > time1:
                          t = threading.Thread(target=self.my_message, args=('Are you sure.... to Submit',))
                          t.start()
                          self.string_for_mbox = "Are sure to Submit"
                          ans = messagebox.askquestion("warning", self.string_for_mbox)
                          if ans == 'yes':
                               t = threading.Thread(target=self.my_message, args=('submit successfuly',))
                               t.start()
                               mycursor = mydb.cursor()

                               sql = "INSERT INTO time_table (day,time1,time2,sub_name,branch,batch) VALUES (%s, %s,%s,%s,%s,%s)"
                               val = (day,time1,time2,sub,branch,batch)
                               mycursor.execute(sql, val)

                               mydb.commit()
                               messagebox.showinfo("success", "Register")

                    else:
                        t = threading.Thread(target=self.my_message, args=('please select valid time',))
                        t.start()
                        messagebox.showerror("Error", "Time Selection Error", icon='warning')
                else:
                    t = threading.Thread(target=self.my_message, args=('please Fill The All Fields',))
                    t.start()
                    messagebox.showerror("Error", "Fill The All Fields", icon='warning')

#root = Tk()
#obj=Timetable()