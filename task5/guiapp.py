import tkinter as tk

def validate_input(value):
    # Check if empty
    if value == "":
        return "empty"

    # Check if numeric
    try:
        number = float(value)
    except ValueError:
        return "not_number"

    # Prevent negative numbers
    if number < 0:
        return "negative"

    return number


def calculate_square(number):
    return number * number


def on_button_click():
    value = entry.get()
    result = validate_input(value)

    if result == "empty":
        result_label.config(text="Error: Input is empty!", fg="red")
    elif result == "not_number":
        result_label.config(text="Error: Please enter a number!", fg="red")
    elif result == "negative":
        result_label.config(text="Error: Negative numbers are not allowed!", fg="red")
    else:
        answer = calculate_square(result)
        result_label.config(text="Result: " + str(answer), fg="green")


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result will appear here", fg="black")


# GUI setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady=10)

calc_button = tk.Button(root, text="Calculate", command=on_button_click)
calc_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=10)

root.mainloop()