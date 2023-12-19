import tkinter as tk
from random import choice

user_score = 0
computer_score = 0

def play_game(player_choice ,root):
    global user_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    show_result(result,root)

def play_again():
    global user_score, computer_score
    userlabel.config(text=('User:', user_score))
    compu_label.config(text=('Computer:', computer_score))
    result_popup.destroy()

def clear():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    userlabel.config(text=('User:', user_score))
    compu_label.config(text=('Computer:', computer_score))

def show_result(result,root):
    global result_popup

    result_popup = tk.Toplevel(root)
    result_popup.title("Result")
    
    result_label = tk.Label(result_popup, text=result, font=("Helvetica", 14)).grid(row = 0, padx=10, pady=10, sticky='w')

    play_again_button = tk.Button(result_popup, text="Play Again", width=15, command=play_again).grid(row=1, column=0, padx=10, pady=10, sticky='w')

    close_button = tk.Button(result_popup, text="Close", command=root.destroy).grid(row=1, column=1, padx=10, pady=10, sticky='w')

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('Rock',root))
rock_button.grid(row=1, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('Paper',root))
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('Scissors',root))
scissors_button.grid(row=1, column=2, padx=10, pady=10)

userlabel = tk.Label(root, text=('User: 0 '), font=("Helvetica", 14))
userlabel.grid(row = 0, column = 0,  padx=10, pady=10, sticky='w') 

compu_label = tk.Label(root, text=('Computer: 0 '), font=("Helvetica", 14))
compu_label.grid(row = 0, column = 2, padx=10, pady=10, sticky='w')

close_button =  tk.Button(root, text="Close", command=root.destroy)
close_button.grid(row=2, column=0, padx=50, pady=10, sticky='w')
clear_button =  tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=2, padx=50, pady=10, sticky='w')
root.mainloop()
