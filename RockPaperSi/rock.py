import tkinter as tk
from random import choice

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('Rock')).grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('Paper')).grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('Scissors')).grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
