import tkinter
import mysql.connector as mysql
from tkinter import ttk
from tkinter import messagebox as mb

# connect database
con = mysql.connect(host="localhost", user="root", password="",database="Python_GUI")
custor = con.cursor()
query = "select id, f_name, l_name, gender, tel_number from tbl_member"
custor.execute(query)
records = custor.fetchall()
print(records[0])

frm = tkinter.Tk()
frm.geometry("1000x500")
frm.title("Display information")

def deldata():
    index = myTree.selection()
    memID = myTree.item(index)["values"]
    delID = str(memID[0])
    res = mb.askyesno("Confirmation", "Do you want to delete this?")
    if res == True:
        myTree.delete(index)
        query = "delete from tbl_member where id = "+delID+""
        custor.execute(query)
        custor.execute("commit")
    else:
        pass


myTree = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5), show="headings")
myTree.pack()

style = ttk.Style()
style.configure("Treeview.Heading", font=('Time New Roman', 16))
style.configure("Treeview", font=('Time New Roman', 14))

myTree.heading(1, text="ID")
myTree.heading(2, text="Firstname", anchor='w')
myTree.heading(3, text="Lastname", anchor='w')
myTree.heading(4, text="Gender")
myTree.heading(5, text="Tel", anchor='w')

myTree.column(1, width=100, anchor='center')
myTree.column(2, width=200, anchor='w')
myTree.column(3, width=300, anchor='w')
myTree.column(4, width=150, anchor='center')
myTree.column(5, width=150, anchor='w')

btn = tkinter.Button(frm, text="Delete",width=15, command=deldata)
btn.place(x=740,y=250)
btn.config(font=('Time New Roman',14), bg='red', fg='white')

# myTree.insert(parent='', index='end', iid=0, text='', values=(1,'Xaypasa', 'Phomkhe','M','99801977'))
# myTree.insert(parent='', index='end', iid=1, text='', values=(2,'obee', 'pom','F','99869069'))

# Loop data from database

val = [1, 2, 3, 4, 5]
global count
count = 0

for x in records:
    myTree.insert(parent='', index='end', iid=count, text='', values=(records[count]))
    count += 1

frm.mainloop()