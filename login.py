from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import collections
from typing import DefaultDict
import mysql.connector
from mysql.connector import connect, connection
import datetime

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1980x1080+0+0")

        self.user=StringVar()
        self.passw=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\one drive-me\OneDrive\Desktop\sai\image\desktop.png")
        
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="#EAEAEA")
        frame.place(x=600,y=250,height=200,width=350)

        title=Label(frame,text="My Library",font=("Algerian",'20'),fg="black",bg="#EAEAEA").place(x=100,y=10)

        lbl_user=Label(frame,text="Username",font=("goudy old style",15),fg="black",bg="#EAEAEA").place(x=50,y=70)
        self.text_user=Entry(frame,textvariable=self.user,font=("arial",10),bg="lightgray").place(x=150,y=70,width=150,height=28)
        
        lbl_pass=Label(frame,text="Password",font=("goudy old style",15),fg="black",bg="#EAEAEA").place(x=50,y=110)
        self.text_pass=Entry(frame,textvariable=self.passw,font=("arial",10),bg="lightgray",show="* ").place(x=150,y=110,width=150,height=28)

        b=Button(frame,command=self.login,text="LOGIN",font=("arial",10),bd=3,relief=RIDGE,bg="white",fg="black")
        b.place(x=120,y=150,width=100,height=30)

 
    
    def login(self):  
        if self.user.get()=="" or self.passw.get()=="":
            messagebox.showerror("ERROR","All fields are required!",parent=self.root)
        elif self.user.get()=="suku" and self.passw.get()=="123":
            self.new_window=Toplevel(self.root)
            self.app=LibraryManagementSystem(self.new_window)
        else:
            messagebox.showerror("ERROR","invalid username and password",parent=self.root)   


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1920x1080+0+0")
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",fg="BLACK",bg="#F2DDC1",font=("algerian",50),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        

        frame=Frame(self.root,bd=12,padx=20,bg="#F2DDC1")
        frame.place(x=0,y=130,width=1530,height=350)

        #*************************variable***************************
 
        self.member_var=StringVar()
        self.reg_var=StringVar()
        self.name_var=StringVar()
        self.mobile_var=StringVar()
        self.email_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.borrowdate_var=StringVar()
        self.duedate_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.actualprice_var=StringVar()       

        #**************data frame left *******************

        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg="#FFF3E4",fg="black",font=("algerian",15,"underline"))
        DataFrameLeft.place(x=0,y=5,width=900,height=313)

        labelmember=Label(DataFrameLeft,bg="#FFF3E4",text="Member Type",font=("arial",12 ),padx=2,pady=4)
        labelmember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12),width=27,state="readonly")
        comMember["value"]=("admin","student","faculty")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblreg_no=Label(DataFrameLeft,bg="#FFF3E4",text="Registration No.",font=("arial",12),padx=2,pady=4)
        lblreg_no.grid(row=1,column=0,sticky=W)
        txtreg_no=Entry(DataFrameLeft,textvariable=self.reg_var,font=("arial",12),width=29)
        txtreg_no.grid(row=1,column=1)

        lblName=Label(DataFrameLeft,bg="#FFF3E4",text="Name",font=("arial",12),padx=2,pady=4)
        lblName.grid(row=2,column=0,sticky=W)
        txtName=Entry(DataFrameLeft,textvariable=self.name_var,font=("arial",12,"bold"),width=29)
        txtName.grid(row=2,column=1)

        lblmobile=Label(DataFrameLeft,bg="#FFF3E4",text="Mobile No.",font=("arial",12),padx=2,pady=4)
        lblmobile.grid(row=3,column=0,sticky=W)
        txtmobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",12),width=29)
        txtmobile.grid(row=3,column=1)
        
        lblEMAIL=Label(DataFrameLeft,bg="#FFF3E4",text="Email",font=("arial",12),padx=2,pady=4)
        lblEMAIL.grid(row=4,column=0,sticky=W)
        txtEMAIL=Entry(DataFrameLeft,textvariable=self.email_var,font=("arial",12),width=29)
        txtEMAIL.grid(row=4,column=1)
        
        labelbookid=Label(DataFrameLeft,bg="#FFF3E4",text="Book-ID",font=("arial",12),padx=40,pady=4)
        labelbookid.grid(row=0,column=2,sticky=W)
        textbookid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",12),width=29)
        textbookid.grid(row=0,column=3)
        
        labelbooktitle=Label(DataFrameLeft,bg="#FFF3E4",text="Book-Title",font=("arial",12),padx=40,pady=4)
        labelbooktitle.grid(row=1,column=2,sticky=W)
        textbooktitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",12),width=29)
        textbooktitle.grid(row=1,column=3)

        labelauthor=Label(DataFrameLeft,bg="#FFF3E4",text="Author",font=("arial",12),padx=40,pady=4)
        labelauthor.grid(row=2,column=2,sticky=W)
        textauthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",12),width=29)
        textauthor.grid(row=2,column=3)

        labelborrowdate=Label(DataFrameLeft,bg="#FFF3E4",text="Borrow Date",font=("arial",12),padx=40,pady=4)
        labelborrowdate.grid(row=3,column=2,sticky=W)
        textborrowdate=Entry(DataFrameLeft,textvariable=self.borrowdate_var,font=("arial",12),width=29)
        textborrowdate.grid(row=3,column=3)

        labelduedate=Label(DataFrameLeft,bg="#FFF3E4",text="Due Date",font=("arial",12),padx=40,pady=4)
        labelduedate.grid(row=4,column=2,sticky=W)
        textduedate=Entry(DataFrameLeft,textvariable=self.duedate_var,font=("arial",12),width=29)
        textduedate.grid(row=4,column=3)
  
        labeldaysonbook=Label(DataFrameLeft,bg="#FFF3E4",text="Days on book",font=("arial",12),padx=40,pady=4)
        labeldaysonbook.grid(row=5,column=2,sticky=W)
        textdaysonbook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",12),width=29)
        textdaysonbook.grid(row=5,column=3)

        labellatereturnfine=Label(DataFrameLeft,bg="#FFF3E4",text="Late Fine",font=("arial",12),padx=40,pady=4)
        labellatereturnfine.grid(row=6,column=2,sticky=W)
        textlatereturnfine=Entry(DataFrameLeft,textvariable=self.latefine_var,font=("arial",12),width=29)
        textlatereturnfine.grid(row=6,column=3)

        labeldateoverdate=Label(DataFrameLeft,bg="#FFF3E4",text="Date over due",font=("arial",12),padx=40,pady=4)
        labeldateoverdate.grid(row=7,column=2,sticky=W)
        textdateoverdate=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",12),width=29)
        textdateoverdate.grid(row=7,column=3)
 
        labelactualprice=Label(DataFrameLeft,bg="#FFF3E4",text="Actual Price",font=("arial",12),padx=40,pady=4)
        labelactualprice.grid(row=8,column=2,sticky=W)
        textactualprice=Entry(DataFrameLeft,textvariable=self.actualprice_var,font=("arial",12),width=29)
        textactualprice.grid(row=8,column=3)
  
        #****************************data frame right ***************************
        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS",bg="#FFF3E4",fg="black",font=("algerian",12,"underline"))
        DataFrameRight.place(x=910,y=5,width=556,height=313)

        self.txtbox=Text(DataFrameRight,font=("arial",10),width=48,height=18,padx=2,pady=0)
        self.txtbox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        listbooks=["Programming in C","Programming in ANSI C","C How To Program","OOP in C++","Programming with C++","DSA","Computer System Architecture","Software Engineering","Python Programming","Database System Concepts","Discrete Mathematics","English Grammar in use","Wings of fire","Godaan","Madhusala","Rashmirathi","Pinjar","Gora"]
        
        def selectbooks(event):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="Programming in C"):
                self.bookid_var.set("B123")
                self.booktitle_var.set("C language")
                self.author_var.set("Balaguruswamy")
                
                d1=datetime.datetime.now()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("Rs.0")

            elif(x=="Programming in ANSI C"):
                self.bookid_var.set("B456")
                self.booktitle_var.set("C language")
                self.author_var.set("Joseph J.")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                x=self.latefine_var.set("Rs.50")
                y=self.dateoverdue_var.set(0)
                self.actualprice_var.set(0) 

            elif(x=="C How To Program"):
                self.bookid_var.set("B789")
                self.booktitle_var.set("C language")
                self.author_var.set("Jackson.M")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("Rs. 0") 

            elif(x=="OOP in C++"):
                self.bookid_var.set("B101")
                self.booktitle_var.set("C++ language")
                self.author_var.set("Navneet Malik")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")  

            
            elif(x=="Programming with C++"):
                self.bookid_var.set("B112")
                self.booktitle_var.set("C++ language")
                self.author_var.set("A.George")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")  

            
            elif(x=="DSA"):
                self.bookid_var.set("B101")
                self.booktitle_var.set("Dsa in c++")
                self.author_var.set("Ranjith kumar")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")  
            
            elif(x=="Computer System Architecture"):
                self.bookid_var.set("B1531")
                self.booktitle_var.set("COD")
                self.author_var.set("Kanwaljeet Singh")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")   
            
            elif(x=="Software Engineering"):
                self.bookid_var.set("B3290")
                self.booktitle_var.set("software Theory")
                self.author_var.set("Vikash Sharma")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")            
            
            elif(x=="Python Programming"):
                self.bookid_var.set("B101")
                self.booktitle_var.set("Python language")
                self.author_var.set("Usha Mittal")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")
            
            elif(x=="Database System Concepts"):
                self.bookid_var.set("B389")
                self.booktitle_var.set("DBMS")
                self.author_var.set("Cherry Joseph")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")   
            
            elif(x=="Discrete Mathematics"):
                self.bookid_var.set("B101")
                self.booktitle_var.set("Discrete")
                self.author_var.set("Pankaj Pandey")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")
            
            elif(x=="English Grammar in use"):
                self.bookid_var.set("B131")
                self.booktitle_var.set("PEL")
                self.author_var.set("Nisha Sharma")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")     
            
            elif(x=="Wings of fire"):
                self.bookid_var.set("B888")
                self.booktitle_var.set("Autobiography")
                self.author_var.set("APJ abdul Kalam")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")              
            
            elif(x=="Godaan"):
                self.bookid_var.set("B111")
                self.booktitle_var.set("Novel")
                self.author_var.set("M.Premchand")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")  
            
            elif(x=="Madhusala"):
                self.bookid_var.set("B7871")
                self.booktitle_var.set("Poetry")
                self.author_var.set("H.R Bachhan")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")  
            
            elif(x=="Rasmirathi"):
                self.bookid_var.set("B555")
                self.booktitle_var.set("Poetry")
                self.author_var.set("Ramdhari singh Dinkar")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")     
            
            elif(x=="Pinjar"):
                self.bookid_var.set("B561")
                self.booktitle_var.set("Novel")
                self.author_var.set("Amrita Pritam")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")       
            
            elif(x=="Gora"):
                self.bookid_var.set("B181")
                self.booktitle_var.set("Novel")
                self.author_var.set("R.Tagore")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.dateoverdue_var.set("0")
                self.actualprice_var.set("0")  

        listbox=Listbox(DataFrameRight,font=("arial",12),width=24,height=15)
        listbox.bind("<<ListboxSelect>>",selectbooks)
        listbox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listbox.yview)

        for item in listbooks:
            listbox.insert(END,item)

        #************** button frame *******************
        framebutton=Frame(self.root,bd=12,padx=20,bg="#FFF3E4")
        framebutton.place(x=0,y=500,width=1530,height=70)

        btnadddata=Button(framebutton,command=self.add_data,text="ADD DATA",font=("arial",12,"bold"),width=23,bg="#F2DDC1",fg="black")
        btnadddata.grid(row=0,column=0)

        btnadddata=Button(framebutton,command=self.showdata,text="SHOW DATA",font=("arial",12,"bold"),width=23,bg="#F2DDC1",fg="black")
        btnadddata.grid(row=0,column=1)

        btnadddata=Button(framebutton,text="UPDATE",command=self.update,font=("arial",12,"bold"),width=23,bg="#F2DDC1",fg="black")
        btnadddata.grid(row=0,column=2)

        btnadddata=Button(framebutton,text="DELETE",command=self.delete,font=("arial",12,"bold"),width=23,bg="#F2DDC1",fg="black")
        btnadddata.grid(row=0,column=3)

        btnadddata=Button(framebutton,command=self.reset,text="RESET",font=("arial",12,"bold"),width=23,bg="#F2DDC1",fg="black")
        btnadddata.grid(row=0,column=4)

        btnadddata=Button(framebutton,text="EXIT",command=self.iExit,font=("arial",12,"bold"),width=23,bg="#F2DDC1",fg="black")
        btnadddata.grid(row=0,column=5)

        #********************* information frame **************************
       
        framedetails=Frame(self.root,relief=FLAT,padx=20,bg="#FFF3E4")
        framedetails.place(x=0,y=600,width=1530,height=200)

        tableframe=Frame(framedetails,bd=6,relief=RIDGE,bg="#FFF3E4")
        tableframe.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.librarytable=ttk.Treeview(tableframe,columns=("membertype","reg_no","name","mobile","email","book_id","book_title","author","borrow_date","due_date","days","late_fine","date_over_due","actual_price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.librarytable.xview)
        yscroll.config(command=self.librarytable.yview)

        self.librarytable.heading("membertype",text="Member Type")
        self.librarytable.heading("reg_no",text="Registration No.")
        self.librarytable.heading("name",text="Name")
        self.librarytable.heading("mobile",text="Mobile No.")
        self.librarytable.heading("email",text="Email")
        self.librarytable.heading("book_id",text="Book-ID")
        self.librarytable.heading("book_title",text="Book-Title")
        self.librarytable.heading("author",text="Author")
        self.librarytable.heading("borrow_date",text="Borrow Date")
        self.librarytable.heading("due_date",text="Due Date")
        self.librarytable.heading("days",text="Days on book")
        self.librarytable.heading("late_fine",text="Late fine")
        self.librarytable.heading("date_over_due",text="Date over due")
        self.librarytable.heading("actual_price",text="Actual price")

        self.librarytable["show"]="headings"
        self.librarytable.pack(fill=BOTH,expand=1)

        self.librarytable.column("membertype",width=100)
        self.librarytable.column("reg_no",width=100)
        self.librarytable.column("name",width=100)
        self.librarytable.column("mobile",width=100)
        self.librarytable.column("email",width=100)
        self.librarytable.column("book_id",width=100)
        self.librarytable.column("book_title",width=100)
        self.librarytable.column("author",width=100)
        self.librarytable.column("borrow_date",width=100)
        self.librarytable.column("due_date",width=100)
        self.librarytable.column("days",width=100)
        self.librarytable.column("late_fine",width=100)
        self.librarytable.column("date_over_due",width=100)
        self.librarytable.column("actual_price",width=100)


        self.fetch_data()
        self.librarytable.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="suku",database="vatsdb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.reg_var.get(),
                                                                                                                self.name_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.email_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.borrowdate_var.get(),
                                                                                                                self.duedate_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.actualprice_var.get()
                                                                                                  ))
        conn.commit()
        self.fetch_data()
        conn.close()        

        messagebox.showinfo("success","member has been inserted successfully")
        return LibraryManagementSystem

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="suku",database="vatsdb")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set member=%s,name=%s,mobile=%s,email=%s,book-id=%s,book-title=%s,author=%s,borrow date=%s,due date=%s,days on book=%s,late fine=%s,date over due=%s,actual price=%s where reg_no=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.name_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.email_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.borrowdate_var.get(),
                                                                                                                self.duedate_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.actualprice_var.get(),
                                                                                                                self.reg_var.get()
                                                                                                    ))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("success","member has been updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="suku",database="vatsdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.librarytable.delete(*self.librarytable.get_children())
            for i in rows:
                self.librarytable.insert("",END,values=i)
            conn.commit()
        conn.close()    

    def get_cursor(self,event=""):
        cursor_row=self.librarytable.focus()
        content=self.librarytable.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0])
        self.reg_var.set(row[1])
        self.name_var.set(row[2])
        self.mobile_var.set(row[3])
        self.email_var.set(row[4])
        self.bookid_var.set(row[5])
        self.booktitle_var.set(row[6])
        self.author_var.set(row[7])
        self.borrowdate_var.set(row[8])
        self.duedate_var.set(row[9])
        self.daysonbook_var.set(row[10])
        self.latefine_var.set(row[11])
        self.dateoverdue_var.set(row[12])
        self.actualprice_var.set(row[13])

    def showdata(self):
        self.txtbox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtbox.insert(END,"Reg no\t\t"+self.reg_var.get()+"\n")
        self.txtbox.insert(END,"Name\t\t"+self.name_var.get()+"\n")
        self.txtbox.insert(END,"Mobile\t\t"+self.mobile_var.get()+"\n")
        self.txtbox.insert(END,"Email\t\t"+self.email_var.get()+"\n")
        self.txtbox.insert(END,"Book id\t\t"+self.bookid_var.get()+"\n")
        self.txtbox.insert(END,"Book title\t\t"+self.booktitle_var.get()+"\n")
        self.txtbox.insert(END,"Author\t\t"+self.author_var.get()+"\n")
        self.txtbox.insert(END,"Borrow date\t\t"+self.borrowdate_var.get()+"\n")
        self.txtbox.insert(END,"Due date\t\t"+self.duedate_var.get()+"\n")
        self.txtbox.insert(END,"Days on book\t\t"+self.daysonbook_var.get()+"\n")
        self.txtbox.insert(END,"Late fine\t\t"+self.latefine_var.get()+"\n")
        self.txtbox.insert(END,"Date over due\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtbox.insert(END,"Actual price\t\t"+self.actualprice_var.get()+"\n")

    def reset(self):
         
        self.member_var.set(""),
        self.reg_var.set(""),
        self.name_var.set(""),
        self.mobile_var.set(""),
        self.email_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.borrowdate_var.set(""),
        self.duedate_var.set(""),
        self.daysonbook_var.set(""),
        self.latefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set(""),
        self.txtbox.delete("1.0",END)   
          
    def iExit(self):
            self.root.destroy()
            return      

    def delete(self):
        if self.reg_var.get()=="" or  self.name_var.get()=="":
            messagebox.showerror("error","first select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="suku",database="vatsdb")
            my_cursor=conn.cursor()
            query="delete from library where reg_no=%s"
            value=(self.reg_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("success","member has been deleted")
            




if __name__=="__main__":
    main()

    # root=Tk()
   #app=Login_Window(root)
    #root.mainloop()