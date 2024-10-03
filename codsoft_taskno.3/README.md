# 3: Password Generator

This project is a Password Generator application built using Tkinter, a standard Python library for creating Graphical User Interfaces (GUIs). The application allows users to specify the length and complexity of the password, and generates a random, strong password based on the user's input.

## How to Run

1. Navigate to the task directory (`codsoft_taskno.3`):
   
    ```bash
   cd codsoft_taskno.3
    ```

3. Run the Python script by executing the following command in your terminal or command prompt:
   
    ```bash
    python password_generator.py
    ```
    
   or, if you're using Python 3:

    ```bash
    python3 password_generator.py
    ```

5. The password generator window will open, where you can enter the desired password length, select the complexity options, and generate a password.

## Features

- User Input: The user can specify the length of the password.
- Complexity Options:
    - Include Uppercase Letters
    - Include Lowercase Letters
    - Include Digits (0-9)
    - Include Special Characters (e.g., @#$%!)
- Clear Button: Clear the current password and reset the input fields.
- Graphical User Interface: Easy-to-use GUI with checkboxes and buttons.


## Example

```bash
python password_generator.py
#Input: Length = 12, select "Include Uppercase Letters", "Include Digits", and "Include Special Characters".
#Output: Generated password is displayed with a yellow highlight, for example:
    Generated Password: X7#D9L!p2*Jq
