from tkinter import messagebox
from tkinter import *
import threading
import pyttsx3
import smtplib
import random
import string
from urllib.request import urlopen
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Keshav@888",
  database="mydatabase",
  auth_plugin='mysql_native_password'
)

class page2(Toplevel):
     def __init__(self):
         Toplevel.__init__(self)
         t = threading.Thread(target=self.my_message, args=('Wellcome',))
         t.start()

         mycursor = mydb.cursor()
         sql = "SELECT * FROM username_password WHERE  sequance ='1'"
         mycursor.execute(sql)
         result = mycursor.fetchone()

         self.email=result[4]
         self.username=result[1]

         self.title("Forgot Username")
         self.Top = Frame(self, height=1200, bg='#A0CFEC')
         self.Top.pack(fill=X)

         self.Button = Button(self.Top, text='Click To Sent Mail To Admin For Forgot Username', bg='green', height=2, width=50,command=lambda :self.clickButton1())
         self.Button.place(x=200, y=70)

         self.label =Label(self.Top, text='Do Not Close This Until Successfully Forgot Username Message Get ', bg='RED', height=1, width=70)
         self.label.place(x=150, y=30)

         self.geometry("800x650+350+50")
         self.resizable(False, False)
         self.mainloop()
     def clickButton1(self):
         t = threading.Thread(target=self.my_message, args=('Are you sure to Forgot password',))
         t.start()
         string_for_mbox = "Are sure to Forgot Username"
         ans = messagebox.askquestion("warning", string_for_mbox)
         if ans=='yes':
             self.username_random = self.randomString()
             connection = self.mailsent()
             if(connection):
                    #print("hlo")
                    #self.username_random=self.randomString()
                    mycursor = mydb.cursor()
                    sql = "UPDATE username_password SET username = %s WHERE  sequance = %s"
                    val = (self.username_random, 1)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    t = threading.Thread(target=self.my_message, args=('Forgot Username successfully and Sent your Mail id',))
                    t.start()
                    messagebox.showinfo("success", "Forgot Username successfully")

     def mailsent(self):
         internet=self.is_internet_available()
         if(internet):
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("iotsmartattendance@gmail.com","KESHAVDS@888")
            message =self.username_random
            s.sendmail("iotsmartattendance@gmail.com", self.email, message)
            s.quit()
            return 1
         else:
             t = threading.Thread(target=self.my_message, args=('please check the internet connection',))
             t.start()
             messagebox.showinfo("Warnnig", "Internet connection not available")
             return  0




     def randomString(self):
         """Generate a random string of fixed length """
         letters = string.ascii_lowercase
         return ''.join(random.choice(letters) for i in range(10))

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

     def is_internet_available(self):
         try:
             urlopen('http://216.58.192.142', timeout=1)
             return 1
         except:
             return 0