
import random
import string
import tkinter as tk

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
        popup = tk.Toplevel(root)
        popup.title("Generated Password")
        # popup.geometry("400x100")
        label = tk.Label(popup, text="Generated Password:")
        label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        password_label = tk.Label(popup, text=password, font=("Arial", 12, "bold"))
        password_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        copy_button = tk.Button(popup, text="Copy Password", command=lambda: root.clipboard_append(password))
        copy_button.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    else:  
        popup = tk.Toplevel(root)
        popup.title("Error")
        # popup.geometry("100x100")
        label = tk.Label(popup, text="Password length Out of Range").pack(padx=50, pady=50)
    
    


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

# Variables to store input and radio button values
plen = tk.IntVar()
include_digit = tk.BooleanVar()
include_symbols = tk.BooleanVar()
include_uppercase = tk.BooleanVar()

# Input bar
label_length = tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=50)

entry_length = tk.Entry(root, textvariable=plen).grid(row=0, column=1 , padx=10, pady=50)

# Radio buttons
checkbutton_digits = tk.Checkbutton(root,text="Include Digits?",  variable=include_digit).grid(row=1, column=0, padx=10, pady=10, sticky='w')


checkbutton_symbols = tk.Checkbutton(root,text="Include Symbols?", variable=include_symbols).grid(row=1, column=1, padx=10, pady=10, sticky='w')


checkbutton_Upper = tk.Checkbutton(root,text="Include uppercase letters?", variable=include_uppercase).grid(row=2, column=0, padx=10, pady=10, sticky='w')


# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, column=0)
close_button = tk.Button(root, text="Close", command=root.destroy).grid(row=3, column=1, columnspan=2)

root.mainloop()