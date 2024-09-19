import tkinter as tk
import random

# Define the possible choices
choices = ['rock', 'paper', 'scissors']

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner of each round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle the user's choice and play the game
def play_game(user_choice):
    global user_score, computer_score

    # Computer makes a random choice
    computer_choice = random.choice(choices)

    # Display the choices
    label_user_choice.config(text=f"You chose: {user_choice}")
    label_computer_choice.config(text=f"Computer chose: {computer_choice}")

    # Determine and display the result
    result = determine_winner(user_choice, computer_choice)
    label_result.config(text=result)

    # Update and display the scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    label_score.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Function to reset the game scores and clear the interface
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="You chose: ")
    label_computer_choice.config(text="Computer chose: ")
    label_result.config(text="Result: ")
    label_score.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Function to clear the current round and play again without resetting scores
def play_again():
    label_user_choice.config(text="You chose: ")
    label_computer_choice.config(text="Computer chose: ")
    label_result.config(text="Result: ")

# Set up the main window with a light blue background
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.config(bg="#ADD8E6")  # Light blue background

# Display labels for the game
label_title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16), bg="#ADD8E6", fg="#00008B")
label_title.grid(row=0, column=0, columnspan=3)

label_user_choice = tk.Label(root, text="You chose: ", font=("Arial", 12), bg="#ADD8E6", fg="#00008B")
label_user_choice.grid(row=1, column=0, columnspan=3)

label_computer_choice = tk.Label(root, text="Computer chose: ", font=("Arial", 12), bg="#ADD8E6", fg="#00008B")
label_computer_choice.grid(row=2, column=0, columnspan=3)

label_result = tk.Label(root, text="Result: ", font=("Arial", 12), bg="#ADD8E6", fg="#00008B")
label_result.grid(row=3, column=0, columnspan=3)

label_score = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12), bg="#ADD8E6", fg="#00008B")
label_score.grid(row=4, column=0, columnspan=3)

# Buttons for user input (Rock, Paper, Scissors)
btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: play_game('rock'), font=("Arial", 12), bg="#FF9999", fg="black")
btn_rock.grid(row=5, column=0)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: play_game('paper'), font=("Arial", 12), bg="#99FF99", fg="black")
btn_paper.grid(row=5, column=1)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('scissors'), font=("Arial", 12), bg="#FFFF99", fg="black")
btn_scissors.grid(row=5, column=2)

# Play Again button to start a new round without resetting scores
btn_play_again = tk.Button(root, text="Play Again", width=10, command=play_again, font=("Arial", 12), bg="#ADD8E6", fg="black")
btn_play_again.grid(row=6, column=0)

# Reset button to restart the game and reset scores
btn_reset = tk.Button(root, text="Reset", width=10, command=reset_game, font=("Arial", 12), bg="#D3D3D3", fg="black")
btn_reset.grid(row=6, column=2)

# Start the Tkinter main event loop
root.mainloop()
