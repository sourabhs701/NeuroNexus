
import random
from tkinter import *
import string

def generate_password():
    length = int(plen.get())
    if (length>0 and length<=100):
        include_digit_val = include_digit.get()
        include_symbol_val = include_symbols.get()
        uppercase_val = include_uppercase.get()

        characters = string.ascii_lowercase
        if include_digit_val:
            characters += string.digits
        if include_symbol_val:
            characters += string.punctuation
        if uppercase_val:
            characters += string.ascii_uppercase

        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Show the generated password in a popup window
        popup =  Toplevel(root)
        popup.title("Generated Password")
        # popup.geometry("400x100")
        label =  Label(popup, text="Generated Password:")
        label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        password_label =  Label(popup, text=password, font=("Arial", 12, "bold"))
        password_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        close_button =  Button(popup, text="Close", command=popup.destroy)
        close_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        copy_button =  Button(popup, text="Copy Password", command=lambda: (root.clipboard_clear(), root.clipboard_append(password)))
        copy_button.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    else:  
        popup =  Toplevel(root)
        popup.title("Error")
        # popup.geometry("100x100")
        label =  Label(popup, text="Password length Out of Range").pack(padx=50, pady=50)
    

#GUI SETUP
root = Tk()
root.title("Password Generator")
root.geometry("400x400")

# Variables to store input and radio button values
plen = IntVar()
include_digit = BooleanVar()
include_symbols = BooleanVar()
include_uppercase = BooleanVar()

# Input bar
label_length =  Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=50)

entry_length =  Entry(root, textvariable=plen).grid(row=0, column=1 , padx=10, pady=50)

# Radio buttons
checkbutton_digits =  Checkbutton(root,text="Include Digits?",  variable=include_digit).grid(row=1, column=0, padx=10, pady=10, sticky='w')

checkbutton_symbols =  Checkbutton(root,text="Include Symbols?", variable=include_symbols).grid(row=1, column=1, padx=10, pady=10, sticky='w')

checkbutton_Upper =  Checkbutton(root,text="Include uppercase letters?", variable=include_uppercase).grid(row=2, column=0, padx=10, pady=10, sticky='w')

# Button to generate password
generate_button =  Button(root, text="Generate Password", command=generate_password).grid(row=3, column=0)
close_button =  Button(root, text="Close", command=root.destroy).grid(row=3, column=1, columnspan=2)

root.mainloop()