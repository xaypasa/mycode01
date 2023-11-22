import tkinter
import mysql.connector as mysql
from tkinter import messagebox
import os


con = mysql.connect(host="localhost", user="root", password="",database="Python_GUI")
custor = con.cursor()

def showpassword():
        if v1.get() == 1:
                en2.config(show="")
        else:
                en2.config(show="*")

def login():
    
        username = en1.get()
        password = en2.get()
        query = "select * from tbl_member where username='"+username+"' and passwd='"+password+"' limit 1"
        custor.execute(query)
        data = custor.fetchone()
        if (data == None):
                messagebox.showinfo("Result","Your username or password incorrect !")
        else:
                frm.destroy()
                os.system("python wwwtest.py")

frm=tkinter.Tk()               
frm.geometry("400x300")
frm.title("Login")

txt1 = tkinter.Label(frm,text="Username: ")
txt1.place(x=30,y=30)
txt1.config(font=('Aptos Display',20))

txt2 = tkinter.Label(frm,text="Password: ")
txt2.place(x=30,y=120)
txt2.config(font=('Aptos Display',20))

v1 = tkinter.IntVar()
c1 = tkinter.Checkbutton(frm, text="Show Password", variable=v1, onvalue=1, offvalue=0,command=showpassword)
c1.place(x=130, y=190)
c1.config(font=('Times New Roman',14))

en1 = tkinter.Entry(frm,width=10)
en1.place(x=187,y=34)
en1.config(font=('Aptos Display',20))

en2 = tkinter.Entry(frm,width=10,show="*")
en2.place(x=187,y=124)
en2.config(font=('Aptos Display',20))

bt1 = tkinter.Button(frm,width=10,text="Login",command= login)
bt1.place(x=60,y=240)
bt1.config(font=('Aptos Display',15),bg="blue",fg="white",border=0)

bt2 = tkinter.Button(frm,width=10,text="Cancel",command=frm.destroy)
bt2.place(x=240,y=240)
bt2.config(font=('Aptos Display',15),bg="Green",fg="white",border=0)


frm.mainloop()
