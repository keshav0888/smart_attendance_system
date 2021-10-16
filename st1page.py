from  tkinter.ttk import *
from numpy import *
from After_login1st import *
from  AdminRegitration import *
from Forgotpu import *
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Keshav@888",
  database="mydatabase",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
root = Tk()
root.title('IoT Based RFID Attendance Monitoring Software')
class login_page(object):
     def  login(self,master):
         self.master = master
         t = threading.Thread(target=self.my_message, args=(
             'I am Smart Bot i will assist you regarding student attendance please enter your credentials',))
         t.start()
         self.Top = Frame(self.master,height=1200, bg='#C0C0C0')
         self.Top.pack(fill=X)

         self.lock=Label(self.Top,font='arial 19 bold', fg="RED" ,bg='#C0C0C0')
         self.lock.place(x=650,y=20)
         def tick():
             time2 = time.strftime('%H:%M:%S')
             self.lock.config(text=time2)
             self.lock.after(200, tick)

         tick()

         self.Top_image = PhotoImage(file='img/icon1.png')
         self.Top_image_label = Label(self.Top, image=self.Top_image,bg='#C0C0C0')
         self.Top_image_label.place(x=10, y=20)
       ##username
         self.username_entry = Entry(self.Top)
         self.username_entry.place(x=340,y=255,width=200,height=30)
         self.username_entry.insert(0, 'Enter the username')

         self.username_entry.bind('<FocusIn>',self.on_entry_click1)
         self.username_entry.bind('<FocusOut>',self.on_focusout1)



         self.username_image = PhotoImage(file='img/username.png')
         self.username_image_lable = Label(self.Top, image=self.username_image, bg='#C0C0C0')
         self.username_image_lable.place(x=280, y=250)

       #password
         self.password_entry = Entry(self.Top)
         self.password_entry.place(x=340, y=310, width=200, height=25)
         self.password_entry.insert(0,'Enter the password')



         self.password_image = PhotoImage(file='img/password3.png')
         self.password_image_lable = Label(self.Top, image=self.password_image, bg='#C0C0C0')
         self.password_image_lable.place(x=280, y=300)

         self.password_entry.bind('<FocusIn>', self.on_entry_click2)
         self.password_entry.bind('<FocusOut>', self.on_focusout2)

       ## checkbox
         self.checkbox = Checkbutton(self.Top, text="Keep me logged in")
         self.checkbox.place(x=345,y=350)

        ##login button
         self.logbtn =Button(self.Top, text="Login", bg="green", fg="White", height=1, width=22, command=lambda: self.login_btn_clicked())
         self.logbtn.place(x=340,y=380)

        ##admin Regitration
         self.admin_label =Button(self.Top, text='Admin Registration', bg='#C0C0C0',height=1,width=13,command=lambda:self.Admin_Register())
         self.admin_label.place(x=280, y=600)

        ##change password/username
         self.forgotpassword_label = Button(self.Top, text='Forgot Username', bg='#C0C0C0', height=1,command=lambda :self.ChangePufun())
         self.forgotpassword_label.place(x=420,y=600)
         root.resizable(False, False)
         root.geometry("800x650+350+50")
         root.mainloop()
     def on_entry_click1(event,master):
          if event.username_entry.get() =='Enter the username':
             event.username_entry.delete(0, "end")  # delete all the text in the entry
             event.username_entry.insert(0, '')  # Insert blank for user input
             event.username_entry.config(fg='black')


     def on_focusout1(event,master):
         if event.username_entry.get() == '':
             event.username_entry.insert(0, 'Enter the username')
             event.username_entry.config(fg='grey')

     def on_entry_click2(event, master):
         if event.password_entry.get() == 'Enter the password':
             event.password_entry.delete(0, "end")  # delete all the text in the entry
             event.password_entry.insert(0, '')  # Insert blank for user input
             event.password_entry.config(fg='black')

     def on_focusout2(event, master):
         if event.password_entry.get() == '':
             event.password_entry.insert(0, 'Enter the password')
             event.password_entry.config(fg='grey')


     def login_btn_clicked(self):
         try:

              username=self.username_entry.get()
              password =self.password_entry.get()
              if len(username) >= 0 and len(password) >= 0:
                 mycursor = mydb.cursor()
                 sql = "SELECT * FROM username_password WHERE  sequance ='1'"
                 mycursor.execute(sql)
                 result = mycursor.fetchone()
                 username_admin=result[1]
                 password_admin=result[2]
                 if username == username_admin and password ==password_admin:
                     obj2=page3()
                 else:
                     t = threading.Thread(target=self.my_message, args=('Invalid Credentials please try again ',))
                     t.start()
                     messagebox.showinfo(self, "Invalid Credentials please try again ")
         except:
             print('Cannot Execute Login function')
             messagebox.showinfo(self, "Cannot Execute Login function")

     def my_message(self,my_message):
         try:

             engine = pyttsx3.init()
             rate= engine.getProperty('rate')
             engine.setProperty('rate',rate- 50)
             engine.say('{}'.format(my_message))
             engine.runAndWait()
             # rate = engine.getProperty('rate')
         except:
             print('Faield to execute my_message function ! ')

     def Admin_Register(self):
          obj3=page1()

     def ChangePufun(self):
         obj4=page2()







def main():
   obj=login_page()
   obj.login(root)

if __name__=="__main__":
     main()





