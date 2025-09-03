import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, ttk
import re

ALLOWED_CHARS = "0123456789+-*/()"

def validate_math(P):
    return all(char in ALLOWED_CHARS for char in P) and len(P) <= 30

root = tk.Tk()
root.title("Shadow's calculator")
root.geometry("300x200")
root.config(bg="darkgrey")
root.resizable(False, False)

icon = tk.PhotoImage(file=r"")  # replace with your file path
root.iconphoto(False, icon)

vcmd = (root.register(validate_math), "%P")

label = tk.Label(root, text="Input:", font=("Arial", 14))
label.pack(pady=5, fill="both", padx=35)

entry = tk.Entry(root, validate="key", validatecommand=vcmd, font=("Arial", 12), width=15)
entry.pack(pady=5, fill="both", padx=15, expand=True)

def get_input(event=None):
    user_text = entry.get().strip()

    user_text = re.sub(r'(\d)\(', r'\1*(', user_text)
    try:
        numbe = eval(user_text)
        result_label.config(text=numbe)
        entry.delete(0, tk.END)
    except Exception as e:
        result_label.config(text=f"Error: {e}")
        entry.delete(0, tk.END)

entry.bind("<Return>", get_input)

label = tk.Label(root, text="Output:", font=("Arial", 14))
label.pack(pady=5, fill="both", padx=35)

result_label = tk.Label(root, text="", font=("Arial", 12), width=15)
result_label.pack(pady=10, padx=15, fill="both", expand=True)

root.mainloop()