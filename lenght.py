import tkinter as tk

def calculate():
    try:
        num1=float(entry1.get())  
        centimeters=num1*2.54
        result_lbl.config(text=f"Centimeters: {centimeters}")
    except ValueError:
        result_lbl.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Inches To Centimeters Calculator")
root.geometry("400x400")

tk.Label(root,text="Enter the number in inches:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

calc_btn = tk.Button(root, text="Calculate", command=calculate, bg="pink")
calc_btn.pack(pady=10)

result_lbl = tk.Label(root, text="Centimeters: ")
result_lbl.pack(pady=5)

root.mainloop()