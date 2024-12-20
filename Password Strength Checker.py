import string
import os
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = password_entry.get()

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, special, digits]
    length = len(password)

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'common.txt')

    try:
        with open(file_path, 'r') as f:
            common = f.read().splitlines()
    except FileNotFoundError:
        messagebox.showerror("Error", f"'common.txt' not found in {script_dir}.")
        return

    if password in common:
        messagebox.showwarning("Weak Password", "Password was found in a common list. Score: 0/7")
        return

    score = 0
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    if score < 4:
        strength = f"Password is weak. Score: {score}/7"
    elif score == 4:
        strength = f"Password is okay. Score: {score}/7"
    elif 4 < score < 6:
        strength = f"Password is good. Score: {score}/7"
    else:
        strength = f"Password is strong. Score: {score}/7"

    messagebox.showinfo("Password Strength", strength)


root = tk.Tk()
root.title("Password Strength Checker")


frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Enter your password:").grid(row=0, column=0, pady=5)
password_entry = tk.Entry(frame, show="*", width=30)
password_entry.grid(row=0, column=1, pady=5)

check_button = tk.Button(frame, text="Check Password", command=check_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)


root.mainloop()
