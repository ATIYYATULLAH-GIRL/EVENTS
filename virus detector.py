from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("300x300")

def msg():
    messagebox.showwarning("Alert"," A VIRUS has been found!!!")
button=Button(window,text="Scan for virus!!!!!!", command=msg)
button.place(x=40,y=80)

window.mainloop()