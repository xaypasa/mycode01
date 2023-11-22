import tkinter

frm = tkinter.Tk()
frm.geometry("500x400")
frm.title("Basic Calculator")
frm.config(bg='lightblue')

def plus():
    number1 = int(txt1.get())
    number2 = int(txt2.get())
    result = number1 + number2
    lb_result.config(text=result)

def minus():
    number1 = int(txt1.get())
    number2 = int(txt2.get())
    result = number1 - number2
    lb_result.config(text=result)

def multiply():
    number1 = int(txt1.get())
    number2 = int(txt2.get())
    result = number1 * number2
    lb_result.config(text=result)

def divided():
    number1 = int(txt1.get())
    number2 = int(txt2.get())
    result = number1 / number2
    lb_result.config(text="%0.2f" % result)
   
lb1 = tkinter.Label(frm, text="Number 1:")
lb1.place(x=10, y=20)
lb1.config(bg='lightblue', font=('Bodoni MT Condensed', 24))

lb2 = tkinter.Label(frm, text="Number 2:")
lb2.place(x=10, y=80)
lb2.config(bg='lightblue', font=('Bodoni MT Condensed', 24))

txt1 = tkinter.Entry(frm)
txt1.place(x=170, y=20)
txt1.config(font=('Bodoni MT Condensed', 24))


txt2 = tkinter.Entry(frm)
txt2.place(x=170, y=80)
txt2.config(font=('Bodoni MT Condensed', 24))

btn1 = tkinter.Button(frm, text="+", width=5, command=plus)
btn1.place(x=100, y=180)
btn1.config(font=('Bodoni MT Condensed', 20))

btn2 = tkinter.Button(frm, text="-", width=5, command=minus)
btn2.place(x=200, y=180)
btn2.config(font=('Bodoni MT Condensed', 20))

btn3 = tkinter.Button(frm, text="X", width=5, command=multiply)
btn3.place(x=300, y=180)
btn3.config(font=('Bodoni MT Condensed', 20))

btn4 = tkinter.Button(frm, text="%", width=5, command=divided)
btn4.place(x=400, y=180)
btn4.config(font=('Bodoni MT Condensed', 20))

lb_result = tkinter.Label(frm, text="Result")
lb_result.place(x=170, y=240)
lb_result.config(bg='lightblue',foreground='red' ,font=('Bodoni MT Condensed',22))

frm.mainloop()

   
    

