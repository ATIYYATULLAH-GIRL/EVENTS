import tkinter as tk

def calculate():
    try:
        num1=float(entry1.get())  
        hectometers=num1*0.01
        result_lbl.config(text=f"Hectometers: {hectometers}")
    except ValueError:
        result_lbl.config(text="Please enter valid numbers.")

root=tk.Tk()
root.title("Meters To Hectometers Calculator")
root.geometry("400x400")

tk.Label(root,text="Enter the number in meters:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

calc_btn = tk.Button(root, text="Calculate", command=calculate, bg="pink")
calc_btn.pack(pady=10)

result_lbl = tk.Label(root, text="Hectometers: ")
result_lbl.pack(pady=5)

root.mainloop()