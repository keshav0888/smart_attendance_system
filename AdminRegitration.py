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
class page1(Toplevel):
     def __init__(self):
         Toplevel.__init__(self)
         t = threading.Thread(target=self.my_message, args=('Wellcome Admin please Complate Your Regitration',))
         t.start()


         self.title("Admin Regitration Page In Student Attendanced System")
         self.Top1 = Frame(self, height=1200, bg='#A0CFEC')
         self.Top1.pack(fill=X)

         self.lock1 = Label(self.Top1, font='arial 19 bold', fg="RED", bg='#A0CFEC')
         self.lock1.place(x=650, y=20)

         def tick1():
             time2 = time.strftime('%H:%M:%S')
             self.lock1.config(text=time2)
             self.lock1.after(200, tick1)

         tick1()

         self.text_lable=Label(self.Top1,text="Admin Registration",font='arial 19 bold', fg="green",width=30,bg='#A0CFEC')
         self.text_lable.place(x=200,y=30)
         self.text_lable_E=Entry(self.Top1,width=20)
         self.text_lable_E.place(x=400,y=100)

         self.name_lable = Label(self.Top1, text="Enter Your name", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.name_lable.place(x=50, y=100)
         self.name_lable_E = Entry(self.Top1, width=20)
         self.name_lable_E.place(x=400, y=100)

         self.Gmail_lable = Label(self.Top1, text="Enter Your Email", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.Gmail_lable.place(x=50, y=150)
         self.Gmail_lable_E = Entry(self.Top1, width=20)
         self.Gmail_lable_E.place(x=400, y=150)

         self.mobailno_lable = Label(self.Top1, text="Enter Your Mobail No", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.mobailno_lable.place(x=70, y=200)
         self.mobailno_lable_E = Entry(self.Top1, width=20)
         self.mobailno_lable_E.place(x=400, y=200)



         self.username_lable = Label(self.Top1, text="Enter Your Username", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.username_lable.place(x=70, y=250)
         self.username_lable_E = Entry(self.Top1, width=20)
         self.username_lable_E.place(x=400, y=250)

         self.password_lable = Label(self.Top1, text="Enter Password ", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.password_lable.place(x=50, y=300)
         self.password_lable_E = Entry(self.Top1, width=20)
         self.password_lable_E.place(x=400, y=300)

         self.cpassword_lable = Label(self.Top1, text="Conform Password ", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.cpassword_lable.place(x=60, y=350)
         self.cpassword_lable_E = Entry(self.Top1, width=20)
         self.cpassword_lable_E.place(x=400, y=350)


         self.pusername_lable = Label(self.Top1, text="Enter Previous Username", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
         self.pusername_lable.place(x=70, y=400)
         self.pusername_lable_E = Entry(self.Top1, width=20)
         self.pusername_lable_E.place(x=400, y=400)

         self.admin_Button=Button(self.Top1,text="Regiter",width=50,bg="green",command=lambda :self.Register())
         self.admin_Button.place(x=200,y=500)

         self.geometry("800x650+350+50")

         self.resizable(False, False)
         self.mainloop()

     def my_message(self,my_message):
             try:

                 engine = pyttsx3.init()
                 rate = engine.getProperty('rate')
                 engine.setProperty('rate', rate - 50)
                 engine.say('{}'.format(my_message))
                 engine.runAndWait()
                 # rate = engine.getProperty('rate')
             except:
                 print('Faield to execute my_message function ! ')

     def Register(self):
          name1=self.name_lable_E.get()
          username1=self.username_lable_E.get()
          mo_no1=self.mobailno_lable_E.get()
          email1=self.Gmail_lable_E.get()
          password1=self.password_lable_E.get()
          cpassword=self.cpassword_lable_E.get()
          pusername=self.pusername_lable_E.get()
          if name1 and username1 and mo_no1 and email1 and password1 and cpassword and pusername!="":
              mycursor = mydb.cursor()
              sql = "SELECT * FROM username_password WHERE  sequance ='1'"
              mycursor.execute(sql)
              result = mycursor.fetchone()
              #print(result[1])
              username_admin = result[1]
              #password_admin = result[2]

              #self.password_admin = result[2]
              #self.name_admin=result[3]
              #self.email_admin=result[4]
              #self.mo_no_admin=result[5]
              #print(result)

              if password1!=cpassword:
                  t = threading.Thread(target=self.my_message, args=('password Not Match',))
                  t.start()
                  messagebox.showinfo("Error", "passaword Not Matching")
              elif pusername !=username_admin:
                     t = threading.Thread(target=self.my_message, args=('please Enter correct previous username',))
                     t.start()
                     messagebox.showinfo("Error", "previous username incorrect")
              else:
                 sequence=1
                 mycursor = mydb.cursor()

                 sql = "DELETE FROM username_password WHERE  sequance = '1'"
                 string_for_mbox = "Are sure to Register"
                 t = threading.Thread(target=self.my_message, args=('Are you sure.... to Regiter',))
                 t.start()
                 ans = messagebox.askquestion("warning", string_for_mbox)
                 if ans == 'yes':
                     # try:
                     mycursor.execute(sql)
                     mydb.commit()
                     mycursor = mydb.cursor()

                     sql = "INSERT INTO username_password (sequance,username,password,name,email,mobail_no ) VALUES (%s, %s,%s,%s,%s,%s)"
                     val = (sequence,username1,password1,name1,email1,mo_no1)
                     mycursor.execute(sql, val)
                     mydb.commit()
                    # query = "select * from username_password where sequence='{}'".format(sequence)
                     #result = cur.execute(query).fetchone()
                     #print(result)
                     t = threading.Thread(target=self.my_message, args=('Regitration successFully completed',))
                     t.start()
                     messagebox.showinfo("success", "Register")
          else:
              t = threading.Thread(target=self.my_message, args=('please Fill The All Fields',))
              t.start()
              messagebox.showerror("Error", "Fill The All Fields", icon='warning')

