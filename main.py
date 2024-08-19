from tkinter import *
from tkinter import messagebox

# Initialize the main window
window = Tk()
window.title("Tic Tac Toe")
window.config(background="#375362")
window.minsize(width=300, height=300)

# X starts so True
clicked = True
count = 0

def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)

def check_if_won():
    global winner
    winner = False

    # Check for winning conditions for X
    for line in winning_combinations:
        if all(buttons[i]["text"] == "X" for i in line):
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins")
            disable_all_buttons()
            return

    # Check for winning conditions for O
    for line in winning_combinations:
        if all(buttons[i]["text"] == "O" for i in line):
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins")
            disable_all_buttons()
            return

    if count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie")
        disable_all_buttons()

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        check_if_won()

    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        clicked = True
        count += 1
        check_if_won()

    else:
        messagebox.showerror("Tic Tac Toe", "This tile is taken!")

def reset():
    global clicked, count
    clicked = True
    count = 0
    for button in buttons:
        button.config(text=" ", state=NORMAL)

# Define winning combinations
winning_combinations = [
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column
    [0, 4, 8],  # Diagonal from top left to bottom right
    [2, 4, 6]   # Diagonal from top right to bottom left
]

# Create buttons
buttons = []
for i in range(9):
    button = Button(window, text=" ", font=("Arial", 20), command=lambda i=i: b_click(buttons[i]), height=3, width=6)
    buttons.append(button)

# Arrange buttons in a grid
for i in range(3):
    for j in range(3):
        buttons[i * 3 + j].grid(row=i, column=j)

# Create a menu
my_menu = Menu(window)
window.config(menu=my_menu)

option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)

window.mainloop()
