import time
from tkinter import *

root=Tk()
root.title("Digital Clock")

lbl=Label(root)
lbl.grid(row=0,column=0)

def display():
    t=time.strftime("%d.%m.%Y\n%I:%M:%S %p")
    lbl.config(text=t, bg='purple', fg='orange', font=('Times New Roman', 50, 'bold'))
    lbl.after(100,display)

display()
root.mainloop()
