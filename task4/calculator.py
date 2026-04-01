import tkinter as tk
from tkinter import messagebox

def calculate():
    user_input = entry.get()

  
    if user_input == "":
        result_label.config(text="Error: Input is empty!", fg="red")
        return

  
    try:
        number = float(user_input)
    except ValueError:
        result_label.config(text="Error: Please enter a valid number!", fg="red")
        return

    if number < 0:
        result_label.config(text="Error: Negative numbers are not allowed!", fg="red")
        return

    
    result = number ** 2

   
    result_label.config(text=f"Result: {result}", fg="green")


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result will appear here", fg="black")


def on_key_release(event):
   
    if entry.get() == "":
        calc_button.config(state="disabled")
    else:
        calc_button.config(state="normal")


root = tk.Tk()
root.title("Improved Calculator")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady=10)

entry.bind("<KeyRelease>", on_key_release)


calc_button = tk.Button(root, text="Calculate", command=calculate, state="disabled")
calc_button.pack(pady=5)


clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack(pady=5)


result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=10)

root.mainloop()