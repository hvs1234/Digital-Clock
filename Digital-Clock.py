#Libraries
from tkinter import * 
from time import strftime

#Application Setup
root = Tk()
root.title("Digital Clock")
root.resizable(False,False)
root.configure(bg="black")

#Functions
def do():
    txt1 = strftime(' %H:%M:%S %p ')
    l1.config(text=txt1)
    l1.after(1000,do)

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\digital clock logo.png")
root.iconphoto(False,img1)
l1 = Label(root,font="digital-7 50 bold",bg="black",fg="lime")
l1.pack(anchor="center")
do()
root.mainloop()
