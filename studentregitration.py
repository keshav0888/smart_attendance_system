from tkinter import messagebox
from tkinter import ttk
import time
from tkinter import *
import threading
import pyttsx3
import tkinter
import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Keshav@888",
  database="mydatabase",
  auth_plugin='mysql_native_password'
)
class student(Toplevel):
    def __init__(self):
        self.state1=DISABLED
        self.var = tkinter.StringVar()
        self.radio_info=""
        Toplevel.__init__(self)
        self.dayValue = StringVar()
        self.dayValue.trace('w',self.limitSizeDay)
        select_batch = tk.StringVar(self)
        select_batch.set("Select Batch")
        select_year = tk.StringVar(self)
        select_year.set("Select Year")
        t = threading.Thread(target=self.my_message, args=('Wellcome......',))
        t.start()

        self.title("Student Regitration Page In Student Attendanced System")
        self.Top1 = Frame(self, height=1200, bg='#C0C0C0')
        self.Top1.pack(fill=X)

        self.lock1 = Label(self.Top1, font='arial 19 bold', fg="RED", bg='#C0C0C0')
        self.lock1.place(x=650, y=20)

        def tick1():
            time2 = time.strftime('%H:%M:%S')
            self.lock1.config(text=time2)
            self.lock1.after(200, tick1)

        tick1()

        self.text_lable = Label(self.Top1, text="Student Registration", font='arial 19 bold', fg="green", width=30,bg='#C0C0C0')
        self.text_lable.place(x=200, y=30)
        self.text_lable_E = Entry(self.Top1, width=20)
        self.text_lable_E.place(x=400, y=100)

        self.name_lable = Label(self.Top1, text="Enter student name", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
        self.name_lable.place(x=50, y=100)
        self.name_lable_E = Entry(self.Top1, width=20)
        self.name_lable_E.place(x=400, y=100)

        self.year_label = Label(self.Top1, text="Select year", font='arial 15 bold', fg="green", width=30, bg='#A0CFEC')
        self.year_label.place(x=50, y=150)
        self.combox_year = ttk.Combobox(self.Top1, width=20, state='readonly', textvariable=select_year)
        self.combox_year['values'] = ('F.Y', 'S.Y', 'T.Y', 'B.E')
        self.combox_year.place(x=400, y=150)

        #self.studyyear_lable = Label(self.Top1, text="Enter Student study Year", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
        #self.studyyear_lable.place(x=50, y=150)
        #self.studyyear_lable_E = Entry(self.Top1, width=20)
        #self.studyyear_lable_E.place(x=400, y=150)

        self.Rollno_lable = Label(self.Top1, text="Enter Student Roll No", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
        self.Rollno_lable.place(x=50, y=200)
        self.Rollno_lable_E = Entry(self.Top1, width=20)
        self.Rollno_lable_E.place(x=400, y=200)

        self.batch_label = Label(self.Top1, text="Select Batch", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
        self.batch_label.place(x=50, y=250)
        self.combox_batch = ttk.Combobox(self.Top1, width=20, state='readonly', textvariable=select_batch)
        self.combox_batch['values'] = ('B1', 'B2', 'B3', 'B4')
        self.combox_batch.place(x=400, y=250)

        self.PRNno_lable = Label(self.Top1, text="Enter Student PRN No", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
        self.PRNno_lable.place(x=50, y=300)
        self.PRNno_lable_E = Entry(self.Top1, width=20)
        self.PRNno_lable_E.place(x=400, y=300)

        self.ratio_lable = Label(self.Top1, text="Enter Student Gender", font='arial 15 bold', fg="green", width=30, bg='#A0CFEC')
        self.ratio_lable.place(x=50, y=350)

        self.R1 = Radiobutton(self.Top1, text="Male",value="Male",variable=self.var,command=lambda:self.radio())
        self.R1.place(x=420,y=350)

        self.R2 = Radiobutton(self.Top1, text="Female",value="Female",variable=self.var,command=lambda:self.radio())
        self.R2.place(x=490,y=350)




        self.mail_lable = Label(self.Top1, text="Enter Student Mail ", font='arial 15 bold', fg="green", width=30,bg='#A0CFEC')
        self.mail_lable.place(x=60, y=400)
        self.mail_lable_E = Entry(self.Top1, width=20)
        self.mail_lable_E.place(x=400, y=400)

        self.smobail_lable = Label(self.Top1, text="Enter Student Mobail no", font='arial 15 bold', fg="green",width=30, bg='#A0CFEC')
        self.smobail_lable.place(x=50, y=450)
        self.smobail_lable_E = Entry(self.Top1, width=20)
        self.smobail_lable_E.place(x=400, y=450)

        self.pmobail_lable = Label(self.Top1, text="Enter Student parent Mobail no", font='arial 15 bold', fg="green",width=30, bg='#A0CFEC')
        self.pmobail_lable.place(x=50, y=500)
        self.pmobail_lable_E = Entry(self.Top1, width=20)
        self.pmobail_lable_E.place(x=400, y=500)


        self.RFIF_Button=Button(self.Top1,text="SCAN CARD",font='arial 13 bold', fg="RED",width=10, bg='#A0CFEC',command=lambda:self.RFID())
        self.RFIF_Button.place(x=590,y=550)

        self.RFID_lable = Label(self.Top1, text="Scan RFID Card To Reader", font='arial 15 bold', fg="green",width=30, bg='#A0CFEC')
        self.RFID_lable.place(x=50, y=550)
        self.RFID_lable_E = Entry(self.Top1, width=20,state=self.state1,textvariable=self.dayValue)
        self.RFID_lable_E.place(x=400, y=550)

        self.SUBMIT_Button=Button(self.Top1,text="SUBMIT",font='arial 15 bold',width=40, bg='green',command=lambda :self.submit())
        self.SUBMIT_Button.place(x=180,y=600)

        t = threading.Thread(target=self.deleterfid)
        t.start()
        self.geometry('800x650+350+50')
        self.resizable(False,False)
        self.mainloop()

    def limitSizeDay(self):
        value = self.dayValue.get()
        if len(value) < 3: self.dayValue.set(value[:2])

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

    def RFID(self):
        self.state1=ACTIVE

        self.RFID_lable_E = Entry(self.Top1, width=20)
        self.RFID_lable_E.place(x=400, y=550)

    def radio(self):
        self.radio_info=self.var.get()



    def submit(self):
        sname=self.name_lable_E.get()
        syear=self.combox_year.get()
        sroll_no=self.Rollno_lable_E.get()
        sPRN=self.PRNno_lable_E.get()
        sgender=self.radio_info
        smail=self.mail_lable_E.get()
        smobail_no=self.mail_lable_E.get()
        spmobail_no=self.pmobail_lable_E.get()
        sRFID=self.RFID_lable_E.get()
        sbatch=self.combox_batch.get()
        if sname and sroll_no and sPRN and smail and smail and smobail_no and spmobail_no and sRFID and sgender!="" and sbatch!="Select Batch" and syear!="Select Year" :
            t = threading.Thread(target=self.my_message, args=('Are you sure.... to Regiter',))
            t.start()
            self.string_for_mbox = "Are sure to Register"
            ans = messagebox.askquestion("warning", self.string_for_mbox)
            if ans == 'yes':
                mycursor = mydb.cursor()

                sql = "INSERT INTO student (sRFID,sname,syear,sroll_no,sbatch,sPRN,sgender,smail,smobail_no,spmobail_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (sRFID,sname,syear,sroll_no,sbatch,sPRN,sgender,smail,smobail_no,spmobail_no)
                mycursor.execute(sql, val)

                mydb.commit()
                t = threading.Thread(target=self.my_message, args=('student Regitration successFully completed',))
                t.start()
                messagebox.showinfo("success", "Register")
        else:
           t = threading.Thread(target=self.my_message, args=('please Fill The All Fields',))
           t.start()
           messagebox.showerror("Error", "Fill The All Fields", icon='warning')
    def deleterfid(self):
          while(1):
              k=str(self.RFID_lable_E.get())
              if(len(k)==11):
                  self.RFID_lable_E.delete(0,10)


