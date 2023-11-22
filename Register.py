import tkinter
import mysql.connector as mysql
import tkinter.messagebox as Messagebox
from tkinter import PhotoImage


con = mysql.connect(host="localhost", user="root", password="",database="Python_GUI")
custor = con.cursor()

def Save():
    name = et_name.get()
    gender = varGender.get()
    tel = et_tel.get()
    email = et_email.get()
    subjects = []

    if varjava.get():
        subjects.append("Java")
    if varpython.get():
        subjects.append("Python")
    if varC.get():
        subjects.append("C#")
    if varReact.get():
        subjects.append("React")

    query = "INSERT INTO tbl_subject (name, gender, tel, email, subject) VALUES (%s, %s, %s, %s, %s)"
    values = (name, gender, tel, email, ', '.join(subjects))

    custor.execute(query, values)
    con.commit()
    
    et_name.delete(0, tkinter.END)
    et_tel.delete(0, tkinter.END)
    et_email.delete(0, tkinter.END)
    cb_subject1.deselect()
    cb_subject2.deselect()
    cb_subject3.deselect()
    cb_subject4.deselect()


        


frm = tkinter.Tk()
frm.geometry("380x500")
frm.title("Register Form")

varGender = tkinter.IntVar()
varGender.set(0)

headTitle = tkinter.Label(frm, text='Choose Subject')
headTitle.pack(pady=(30))
headTitle.config(font=('Noto Sans Lao', 15, 'bold'))

# Label
lb_name = tkinter.Label(frm, text='Fullname:')
lb_name.place(x=30, y=80)
lb_name.config(font=('Noto Sans Lao', 13, 'bold'))

lb_gender = tkinter.Label(frm, text='Gender:')
lb_gender.place(x=30, y=130)
lb_gender.config(font=('Noto Sans Lao', 13, 'bold'))

lb_tel = tkinter.Label(frm,text='tel:')
lb_tel.place(x=30,y=175)
lb_tel.config(font=('Noto Sans Lao', 13, 'bold'))

lb_email = tkinter.Label(frm,text='e-mail:')
lb_email.place(x=30,y=220)
lb_email.config(font=('Noto Sans Lao', 13, 'bold'))

lb_subject = tkinter.Label(frm,text='Subject:')
lb_subject.place(x=30,y=265)
lb_subject.config(font=('Noto Sans Lao', 13, 'bold'))

bt_save = tkinter.Button(frm,text='Save',command=Save)
bt_save.place(x=30,y=365)
bt_save.config(font=('Noto Sans Lao', 20, 'bold'))

bt_cancel = tkinter.Button(frm,text='Cancel',command=frm.destroy)
bt_cancel.place(x=230,y=365)
bt_cancel.config(font=('Noto Sans Lao', 20, 'bold'))

et_name = tkinter.Entry(frm)
et_name.place(x=120,y=80)
et_name.config(font=('Noto Sans Lao', 13, 'bold'))

rb_gender1 = tkinter.Radiobutton(frm,text='Male',variable=varGender,value=1)
rb_gender1.place(x=120,y=130)
rb_gender1.config(font=('Noto Sans Lao', 14, 'bold'))

rb_gender2 = tkinter.Radiobutton(frm,text='Female',variable=varGender,value=2)
rb_gender2.place(x=220,y=130)
rb_gender2.config(font=('Noto Sans Lao', 14, 'bold'))

et_tel = tkinter.Entry(frm)
et_tel.place(x=120,y=175)
et_tel.config(font=('Noto Sans Lao', 13, 'bold'))

et_email = tkinter.Entry(frm)
et_email.place(x=120,y=220)
et_email.config(font=('Noto Sans Lao', 13, 'bold'))

varjava = tkinter.IntVar()
cb_subject1 = tkinter.Checkbutton(frm,text='Java',variable=varjava, onvalue=1, offvalue=0)
cb_subject1.place(x=120,y=265)
cb_subject1.config(font=('Noto Sans Lao', 13, 'bold'))

varpython = tkinter.IntVar()
cb_subject2 = tkinter.Checkbutton(frm,text='Python',variable=varpython, onvalue=1, offvalue=0)
cb_subject2.place(x=220,y=265)
cb_subject2.config(font=('Noto Sans Lao', 13, 'bold'))

varC = tkinter.IntVar()
cb_subject3 = tkinter.Checkbutton(frm,text='C#',variable=varC, onvalue=1, offvalue=0)
cb_subject3.place(x=120,y=310)
cb_subject3.config(font=('Noto Sans Lao', 13, 'bold'))

varReact = tkinter.IntVar()
cb_subject4 = tkinter.Checkbutton(frm,text='react',variable=varReact, onvalue=1, offvalue=0)
cb_subject4.place(x=220,y=310)
cb_subject4.config(font=('Noto Sans Lao', 13, 'bold'))

frm.mainloop()
