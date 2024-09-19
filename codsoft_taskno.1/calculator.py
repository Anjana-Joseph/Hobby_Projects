import tkinter as tk

calculation = ""

# Function to add symbols to the calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")    

# Function to clear the input field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Set up the main application window
root = tk.Tk()
root.geometry("300x275")
root.config(bg="dark grey")

# Text field to display the input and result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="light grey", fg="black")
text_result.grid(columnspan=5)

# List of buttons with text, row, and column
buttons = [
    ('1', 4, 1), ('2', 4, 2), ('3', 4, 3),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
    ('7', 2, 1), ('8', 2, 2), ('9', 2, 3), ('0', 5, 2),
    ('/', 2, 4), ('*', 3, 4), ('-', 4, 4), ('+', 5, 4), ('(', 5, 1), (')', 5, 3),
    ('C', 6, 1), ('.', 6, 2), ('=', 6, 3, 2)
]

# To handle button commands based on text
def button_command(text):
    if text == "=":
        evaluate_calculation()
    elif text == "C":
        clear_field()
    else:
        add_to_calculation(text)

# To create buttons
for button_info in buttons:
    text, row, column = button_info[:3]  # Extract text, row, and column
    span = button_info[3] if len(button_info) == 4 else 1  # Handle optional column span

    # Create a button with appropriate text and action
    btn = tk.Button(root, text=text, command=lambda t=text: button_command(t), 
                    width=5, font=("Arial", 14), bg="grey", fg="white")

    # Set the button position in the grid
    btn.grid(row=row, column=column, columnspan=span)

root.mainloop()
