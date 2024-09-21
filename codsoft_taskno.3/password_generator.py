import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password based on user input
def generate_password():
    try:
        # Get the desired password length from the user
        length = int(entry_length.get())
        if length < 1:
            raise ValueError

        # Initialize an empty string for possible characters based on user selection
        characters = ""

        # Add character types based on user selection
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_lowercase.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        # If no character types are selected, raise an error
        if not characters:
            raise ValueError("Please select at least one character type.")

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
label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="light blue")
label_length.pack()

# Entry widget for user to input the desired password length
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=5)

# Options for password complexity (checkboxes)
label_complexity = tk.Label(root, text="Select Password Complexity:", font=("Arial", 12), bg="light blue")
label_complexity.pack(pady=5)

# Boolean variables to track the state of each checkbox
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

# Checkbuttons for each character type
chk_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", font=("Arial", 12), bg="light blue", variable=var_uppercase)
chk_uppercase.pack()

chk_lowercase = tk.Checkbutton(root, text="Include Lowercase Letters", font=("Arial", 12), bg="light blue", variable=var_lowercase)
chk_lowercase.pack()

chk_digits = tk.Checkbutton(root, text="Include Digits", font=("Arial", 12), bg="light blue", variable=var_digits)
chk_digits.pack()

chk_symbols = tk.Checkbutton(root, text="Include Special Characters", font=("Arial", 12), bg="light blue", variable=var_symbols)
chk_symbols.pack()

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
