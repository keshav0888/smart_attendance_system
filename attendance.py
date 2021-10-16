from tkinter import *
#import threading
import pyttsx3
import datetime
import time
import threading
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Keshav@888",
  database="mydatabase",
  auth_plugin='mysql_native_password'
)

class attendance(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        t = threading.Thread(target=self.my_message, args=('Wellcome......',))
        t.start()

        self.title(" Option Page In Student Attendanced System")
        self.Top1 = Frame(self, height=1200, bg='#C0C0C0')
        self.Top1.pack(fill=X)

        self.lock1 = Label(self.Top1, font='arial 19 bold', fg="RED", bg='#C0C0C0')
        self.lock1.place(x=650, y=20)

        self.label1=Label(self.Top1, text="INPUT RFID NUMBER",font='arial 19 bold', fg="RED", bg='#C0C0C0')
        self.label1.place(x=270,y=130)

        self.entry1=Entry(self.Top1,width=50,border=10)
        self.entry1.place(x=200,y=200)
        def tick1():
            time2 = time.strftime('%H:%M:%S')
            self.lock1.config(text=time2)
            self.lock1.after(200, tick1)

        tick1()

        t1 = threading.Thread(target=self.fun)
        t1.start()
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
    def fun(self):
       self.i=1
       while(1):
          k=str(self.entry1.get())
          if(len(k)==10 and self.i==1):
              self.fun1()
              self.i=0
          if(len(k)==11):
              self.entry1.delete(0,10)
              self.i=1

    def fun1(self):
        print(self.entry1.get())



