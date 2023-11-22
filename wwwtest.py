import tkinter
import mysql.connector as mysql
import tkinter.messagebox

con = mysql.connect(host="localhost", user="root", password="",database="Python_GUI")
custor = con.cursor()

frm = tkinter.Tk()
frm.geometry("600x600")
frm.title("Register")

varGender = tkinter.IntVar()
varGender.set(1)


def register():
    if io5.get() != io6.get():
         tkinter.messagebox.showerror("password error","Retry")
    else:
        firstname = io1.get()
        lastname = io2.get()
        gender = varGender.get()
        tel = io3.get()
        username = io4.get()
        password = io5.get()
    
   
        query = "INSERT INTO tbl_member (f_name, l_name, gender, tel_number, username, passwd) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (firstname, lastname, gender, tel, username, password)
        custor.execute(query,values)
        con.commit()

        io1.delete(0, tkinter.END)
        io2.delete(0, tkinter.END)
        io3.delete(0, tkinter.END)
        io4.delete(0, tkinter.END)
        io5.delete(0, tkinter.END)
        io6.delete(0, tkinter.END)

    

txt1 = tkinter.Label(frm,text = "Firstname: ")
txt1.place(x=20,y=20)
txt1.config(font=('Bahnschrift Condensed',24))

txt2 = tkinter.Label(frm,text = "Lastname: ")
txt2.place(x=20,y=80)
txt2.config(font=('Bahnschrift Condensed',24))

txt3 = tkinter.Label(frm,text = "Gender: ")
txt3.place(x=20,y=150)
txt3.config(font=('Bahnschrift Condensed',24))

txt4 = tkinter.Label(frm,text = "Tel: ")
txt4.place(x=20,y=220)
txt4.config(font=('Bahnschrift Condensed',24))

txt5 = tkinter.Label(frm,text = "Username: ")
txt5.place(x=20,y=280)
txt5.config(font=('Bahnschrift Condensed',24))

txt6 = tkinter.Label(frm,text = "Password: ")
txt6.place(x=20,y=350)
txt6.config(font=('Bahnschrift Condensed',24))

txt7 = tkinter.Label(frm,text = "Confirm: ")
txt7.place(x=20,y=420)
txt7.config(font=('Bahnschrift Condensed',24))

rd1 = tkinter.Radiobutton(frm,text="Male",variable=varGender, value=1)
rd1.place(x=170,y=150)
rd1.config(font=('Bahnschrift Condensed',20))

rd2 = tkinter.Radiobutton(frm,text="Female",variable=varGender, value=2)
rd2.place(x=290,y=150)
rd2.config(font=('Bahnschrift Condensed',20))

bt1 = tkinter.Button(frm,text="Register",width=14,height=1,command= register)
bt1.place(x=150,y=500)
bt1.config(font=('Bahnschrift Condensed',20))

bt2 = tkinter.Button(frm,text="Cancel",width=14,height=1,command= frm.destroy)
bt2.place(x=340,y=500)
bt2.config(font=('Bahnschrift Condensed',20))

io1 = tkinter.Entry(frm,width=20)
io1.place(x=180,y=30)
io1.config(font=('Bahnschrift Condensed',20, 'bold'))

io2 = tkinter.Entry(frm,width=20)
io2.place(x=180,y=90)
io2.config(font=('Bahnschrift Condensed',20, 'bold'))

io3 = tkinter.Entry(frm,width=20)
io3.place(x=180,y=230)
io3.config(font=('Bahnschrift Condensed',20))

io4 = tkinter.Entry(frm,width=20)
io4.place(x=180,y=290)
io4.config(font=('Bahnschrift Condensed',20))

io5 = tkinter.Entry(frm,width=20,show="*")
io5.place(x=180,y=360)
io5.config(font=('Bahnschrift Condensed',20))

io6 = tkinter.Entry(frm,width=20,show="*")
io6.place(x=180,y=430)
io6.config(font=('Bahnschrift Condensed',20))

frm.mainloop()