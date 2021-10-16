from tkinter import messagebox
import datetime
import time
from tkinter import *
import threading
import pyttsx3
from attendance import *
from  studentregitration import *
from Timetable import *
class page3(Toplevel):
     def __init__(self):
         Toplevel.__init__(self)
         t = threading.Thread(target=self.my_message, args=('Wellcome......',))
         t.start()

         self.title(" Option Page In Student Attendanced System")
         self.Top1 = Frame(self, height=1200, bg='#C0C0C0')
         self.Top1.pack(fill=X)



         self.lock1 = Label(self.Top1, font='arial 19 bold', fg="RED", bg='#C0C0C0')
         self.lock1.place(x=650, y=20)
         def tick1():
             time2 = time.strftime('%H:%M:%S')
             self.lock1.config(text=time2)
             self.lock1.after(200, tick1)

         tick1()

         self.admin_Button = Button(self.Top1, text="Course Time Table Regitration", width=50, bg="green",command=lambda: self.Timetable())
         self.admin_Button.place(x=200, y=50)

         self.admin_Button1 = Button(self.Top1, text="Student Regitration", width=50, bg="green", command=lambda: self.studentregitration())
         self.admin_Button1.place(x=200, y=100)

         self.admin_Button2 = Button(self.Top1, text="Attendance", width=50, bg="green",command=lambda: self.attendance())
         self.admin_Button2.place(x=200, y=150)

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



     def studentregitration(self):
         obj=student()

     def Timetable(self):
         obj1=Timetable()

     def attendance(self):
          obj2=attendance()