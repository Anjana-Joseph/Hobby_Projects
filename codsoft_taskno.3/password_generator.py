import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password based on the selected strength
def generate_password():
    try:
        # Get the desired password length from the user
        length = int(entry_length.get())
        if length < 1:
            raise ValueError

        # Initialize an empty string for possible characters
        characters = ""

        # Add character types based on the selected strength
        strength = var_strength.get()

        if strength == 1:  # Weak: Only lowercase letters
            characters = string.ascii_lowercase
        elif strength == 2:  # Medium: Lowercase letters and digits
            characters = string.ascii_lowercase + string.digits
        elif strength == 3:  # Strong: Lowercase, uppercase, digits, and special characters
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Please select a password strength.")

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password with a background highlight
        label_password.config(text=f"Generated Password: {password}", bg="yellow")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Function to clear the input and output fields
def clear_fields():
    entry_length.delete(0, tk.END)
    label_password.config(text="Generated Password: ", bg="light blue")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="light blue")

# Title Label
label_title = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="light blue")
label_title.pack(pady=10)

# Label for password length input
label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12, "bold"), bg="light blue")
label_length.pack()

# Entry widget for user to input the desired password length
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=5)

# Label for password strength selection
label_strength = tk.Label(root, text="Select Password Strength:", font=("Arial", 12, "bold"), bg="light blue")
label_strength.pack(pady=5)

# Radio buttons for password strength selection
var_strength = tk.IntVar()
var_strength.set(0)  # Default is none selected

# Radio button for weak password
radio_weak = tk.Radiobutton(root, text="Weak (Lowercase Letters)", variable=var_strength, value=1, font=("Arial", 12), bg="light blue")
radio_weak.pack()

# Radio button for medium password
radio_medium = tk.Radiobutton(root, text="Medium (Lowercase + Digits)", variable=var_strength, value=2, font=("Arial", 12), bg="light blue")
radio_medium.pack()

# Radio button for strong password
radio_strong = tk.Radiobutton(root, text="Strong (Letters + Digits + Symbols)", variable=var_strength, value=3, font=("Arial", 12), bg="light blue")
radio_strong.pack()

# Label to display the generated password with background highlight
label_password = tk.Label(root, text="Generated Password: ", font=("Arial", 12, "bold"), bg="light blue")
label_password.pack(pady=5)

# Create a frame to hold the buttons side by side
button_frame = tk.Frame(root, bg="light blue")
button_frame.pack(pady=10)

# Button to generate the password, placed in the button frame
btn_generate = tk.Button(button_frame, text="Generate Password", font=("Arial", 12), command=generate_password, bg="blue", fg="white")
btn_generate.grid(row=0, column=0, padx=5)

# Clear button, placed next to the generate button in the button frame
btn_clear = tk.Button(button_frame, text="Clear", font=("Arial", 12), command=clear_fields, bg="grey", fg="white")
btn_clear.grid(row=0, column=1, padx=5)

# Start the Tkinter main event loop
root.mainloop()
