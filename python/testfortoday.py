import tkinter

def multiply():
    number1 = int(io1.get())
    number2 = int(io2.get())
    result = number1 * number2
    txt_result1.config(text=result)

def ogee():
    number1 = int(io3.get())
    number2 = int(io4.get())
    result = number1 * number2
    txt_result2.config(text=result/2)

def good():
    number1 = int(io5.get())
    bob = number1/2
    result = bob * bob * 3.14
    txt_result3.config(text=result)

frm = tkinter.Tk()
frm.geometry("1300x500")
frm.config(bg='#404565')
frm.title("Final Test")

txt1 = tkinter.Label(frm,text="ຮູບສີ່ແຈສາກ")
txt1.place(x=20,y=20)
txt1.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',24))

txt2 = tkinter.Label(frm,text="ລວງຍາວ: ")
txt2.place(x=20,y=90)
txt2.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',18))

txt3 = tkinter.Label(frm,text="ລວງກວ້າງ: ")
txt3.place(x=20,y=150)
txt3.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',18))

txt4 = tkinter.Label(frm,text="ຮູບສາມແຈສາກ")
txt4.place(x=390,y=20)
txt4.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',24))

txt5 = tkinter.Label(frm,text="ຂ້າງພື້ນ: ")
txt5.place(x=390,y=90)
txt5.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',18))

txt6 = tkinter.Label(frm,text="ລວງສູງ: ")
txt6.place(x=390,y=150)
txt6.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',18))

txt7 = tkinter.Label(frm,text="ຮູບວົງມົນ")
txt7.place(x=790,y=20)
txt7.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',24))

txt8 = tkinter.Label(frm,text="ເສັ້ນຜ່າສູນກາງ: ")
txt8.place(x=790,y=90)
txt8.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',18))

bt1 = tkinter.Button(frm,text="ຄຳນວນເນື້ອທີ່",width=16,height=1,command=multiply)
bt1.place(x=30,y=210)
bt1.config(font=('Phetsarath OT',16))

bt2 = tkinter.Button(frm,text="ຄຳນວນເນື້ອທີ່",width=16,height=1,command=ogee)
bt2.place(x=400,y=210)
bt2.config(font=('Phetsarath OT',16))

bt3 = tkinter.Button(frm,text="ຄຳນວນເນື້ອທີ່",width=16,height=1,command=good)
bt3.place(x=800,y=163)
bt3.config(font=('Phetsarath OT',16))

io1 = tkinter.Entry(frm,width=7)
io1.place(x=130,y=90)
io1.config(font=('Phetsarath OT',18))

io2 = tkinter.Entry(frm,width=7)
io2.place(x=130,y=150)
io2.config(font=('Phetsarath OT',18))

io3 = tkinter.Entry(frm,width=7)
io3.place(x=490,y=90)
io3.config(font=('Phetsarath OT',18))

io4 = tkinter.Entry(frm,width=7)
io4.place(x=490,y=150)
io4.config(font=('Phetsarath OT',18))

io5 = tkinter.Entry(frm,width=7)
io5.place(x=940,y=90)
io5.config(font=('Phetsarath OT',18))

txt_result1 = tkinter.Label(frm,text="#####")
txt_result1.place(x=70,y=310)
txt_result1.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',20))

txt_result2 = tkinter.Label(frm,text="#####")
txt_result2.place(x=440,y=310)
txt_result2.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',20))

txt_result3 = tkinter.Label(frm,text="#####")
txt_result3.place(x=850,y=260)
txt_result3.config(fg='#ffffff',bg='#404565',font=('Phetsarath OT',20))


frm.mainloop()