import tkinter

frm = tkinter.Tk()
frm.geometry("400x600")
frm.title("input your information")
frm.config(bg='#4987f8')

def regis():
    fn = text1.get()
    ln = text2.get()
    ag = text3.get()
    fs = [fn,ln,ag]
    if len(fn) != 0 and len(ln) != 0 and ag != "0":
    
        
        with open('register.txt',"a") as f:
            f.write(str(fs)+'\n')
        
        text1.delete(0,'end')
        text2.delete(0,'end')
        text3.delete(0,'end')
        text1.focus()



a = tkinter.Label(frm, text="input your information")
a.place(x=0)
a.config(fg='#4987f8', width=37, bg='white',font=('Bodoni MT Condensed',23))

a1 = tkinter.Label(frm, text="Firstname: ")
a1.place(x=10,y=50)
a1.config(fg='white', bg='#4987f8',font=('Bodoni MT Condensed',23))

a2 = tkinter.Label(frm, text="Lastname: ")
a2.place(x=10,y=120)
a2.config(fg='white', bg='#4987f8',font=('Bodoni MT Condensed',23))

a3 = tkinter.Label(frm, text="Age: ")
a3.place(x=10,y=190)
a3.config(fg='white', bg='#4987f8',font=('Bodoni MT Condensed',23))

text1 = tkinter.Entry(frm)
text1.place(x=120,y=50)
text1.config(font=('Bodoni MT Condensed',23))

text2 = tkinter.Entry(frm)
text2.place(x=120,y=120)
text2.config(font=('Bodoni MT Condensed',23))

text3 = tkinter.Entry(frm,width=8)
text3.place(x=120,y=190)
text3.config(font=('Bodoni MT Condensed',23))

button1 = tkinter.Button(frm,text="Register",width=25,command=regis)
button1.place(x=120,y=240)
button1.config(bg='white', fg='#4987f8' ,font=('Bodoni MT Condensed',18))


frm.mainloop()
