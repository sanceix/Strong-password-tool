import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# -----------------------------
# Function to generate password
# -----------------------------
def generate_password():
    try:
        length = int(length_entry.get())  # Get length from user input
        if length < 4:
            raise ValueError  # Raise error for very short lengths

        # Combine all possible characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Randomly pick characters
        password = ''.join(random.choice(characters) for _ in range(length))

        # Show generated password in entry box
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        validate_password()  # Auto-check password strength

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number greater than 3.")

# ----------------------------------------
# Function to check password strength
# ----------------------------------------
def validate_password():
    password = password_entry.get()
    strength = 0  # Initial strength score
    feedback = ""  # Message to show user

    # Check each rule and give 1 point per match
    if len(password) >= 8:
        strength += 1
    else:
        feedback = "❌ Too short"

    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback = "❌ Add uppercase letters"

    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback = "❌ Add lowercase letters"

    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback = "❌ Add numbers"

    if any(c in string.punctuation for c in password):
        strength += 1
    else:
        feedback = "❌ Add special characters"

    # Set strength bar value
    progress['value'] = strength * 20  # Each point is 20%

    # Change bar color based on score
    if strength <= 2:
        style.configure("TProgressbar", foreground="red", background="red")
    elif strength == 3:
        style.configure("TProgressbar", foreground="orange", background="orange")
    elif strength == 4:
        style.configure("TProgressbar", foreground="gold", background="gold")
    else:
        style.configure("TProgressbar", foreground="green", background="green")

    # Show strength message
    if strength == 5:
        result_label.config(text="✅ Strong Password", fg="lightgreen")
    else:
        result_label.config(text=feedback, fg="red")

# ----------------------------------------
# Function to copy password to clipboard
# ----------------------------------------
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ----------------------------------------
# Function to show/hide password text
# ----------------------------------------
def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text="👁 Show")
    else:
        password_entry.config(show='')
        toggle_btn.config(text="🙈 Hide")

# ----------------------------------------
# Setup main window
# ----------------------------------------
root = tk.Tk()
root.title("🔐 Strong Password Generator")
root.geometry("450x400")  # Window size
root.resizable(False, False)
root.configure(bg="#2C3E50")  # Background color

# Progress bar style
style = ttk.Style(root)
style.theme_use('clam')  # Use modern flat look
style.configure("TProgressbar", thickness=20)

# -------------------------
# GUI ELEMENTS BELOW
# -------------------------

# Title
tk.Label(root, text="🛡 Password Generator & Checker", bg="#2C3E50",
         fg="white", font=("Helvetica", 16, "bold")).pack(pady=15)

# Input for password length
tk.Label(root, text="Enter password length:", bg="#2C3E50", fg="white",
         font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
length_entry.pack(pady=5)

# Generate password button
tk.Button(root, text="⚙️ Generate Password", font=("Arial", 12), command=generate_password,
          bg="#1ABC9C", fg="white").pack(pady=10)

# Password Entry (where password shows)
tk.Label(root, text="Generated or Your Password:", bg="#2C3E50", fg="white",
         font=("Arial", 12)).pack()

# Frame to hold password + toggle button
password_frame = tk.Frame(root, bg="#2C3E50")
password_frame.pack(pady=5)

password_entry = tk.Entry(password_frame, font=("Arial", 12), width=30,
                          justify='center', show='*')  # default hidden
password_entry.pack(side=tk.LEFT, padx=5)

toggle_btn = tk.Button(password_frame, text="👁 Show", command=toggle_password,
                       bg="#34495E", fg="white")
toggle_btn.pack(side=tk.LEFT)

# Validate button
tk.Button(root, text="🔎 Check Password Strength", font=("Arial", 12),
          command=validate_password, bg="#3498DB", fg="white").pack(pady=10)

# Progress bar to show strength
progress = ttk.Progressbar(root, length=300, mode='determinate', maximum=100,
                           style="TProgressbar")
progress.pack(pady=10)

# Feedback label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2C3E50", fg="white")
result_label.pack(pady=5)

# Copy button
tk.Button(root, text="📋 Copy to Clipboard", font=("Arial", 11), command=copy_to_clipboard,
          bg="#E67E22", fg="white").pack(pady=10)

# Start GUI loop
root.mainloop()
