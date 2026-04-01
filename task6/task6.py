import tkinter as tk
from tkinter import messagebox

def submit():
    student_name = name_entry.get()
    student_age = age_entry.get()
    student_grade = grade_entry.get()

    if student_name == "":
        messagebox.showerror("Error", "Name cannot be empty!")
        return
    if not student_age.isdigit():
        messagebox.showerror("Error", "Age must be a number!")
        return
    if student_grade == "":
        messagebox.showerror("Error", "Grade cannot be empty!")
        return

    result_label.config(
        text=f"Student: {student_name}\nAge: {student_age}\nGrade: {student_grade}"
    )

def clear():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    result_label.config(text="")


root = tk.Tk()
root.title("Student Information Form")
root.geometry("350x250")


tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Grade:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=4, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="w")

root.mainloop()