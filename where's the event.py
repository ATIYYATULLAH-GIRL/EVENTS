from tkinter import *

window=Tk()
window.title("Event Handler")
window.geometry("200x100")

def handle_key_press(event):
    print(event.char)
window.bind("<Key>",handle_key_press)
button=Button(text="Click Me")
button.pack()

def handle_click(event):
    print("The button was clicked")
button.bind("<Button-1>",handle_click)

window.mainloop()