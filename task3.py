import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Password: {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")


root = tk.Tk()
root.title("Simple Password Generator")


tk.Label(root, text="Enter password length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="Password: ")
result_label.pack(pady=10)

root.mainloop()