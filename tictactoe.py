import tkinter as tk
from tkinter import messagebox

def print_tic_tac_toe(values):
    for i in range(3):
        for j in range(3):
            button = buttons[i*3+j]
            button.config(text=values[i*3+j])
            if values[i*3+j] == ' ':
                button.config(state='normal')
            else:
                button.config(state='disabled')

def check_win(player_pos, cur_player):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            return True
    return False

def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

def single_game(button):
    global cur_player
    move = buttons.index(button) + 1
    values[move-1] = cur_player
    player_pos[cur_player].append(move)
    print_tic_tac_toe(values)
    if check_win(player_pos, cur_player):
        messagebox.showinfo("Winner", "Player " + cur_player + " has won the game!!")
        score_board[cur_player] += 1
        print_scoreboard()
        reset_game()
        return
    if check_draw(player_pos):
        messagebox.showinfo("Draw", "Game Drawn")
        reset_game()
        return
    if cur_player == 'X':
        cur_player = 'O'
    else:
        cur_player = 'X'

def reset_game():
    global values
    global player_pos
    global cur_player
    values = [' ' for x in range(9)]
    player_pos = {'X':[], 'O':[]}
    cur_player = 'X'
    for i, button in enumerate(buttons):
        button.config(text=str(i+1))
        button.config(state='normal')

def get_player_names():
    def submit_names(): 
        global player1_name
        global player2_name
        player1_name = player1_entry.get()
        player2_name = player2_entry.get()
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Enter Player Names")
    
    player1_label = tk.Label(top, text="Player X Name:")
    player1_label.pack()
    
    player1_entry = tk.Entry(top)
    player1_entry.pack()
    
    player2_label = tk.Label(top, text="Player O Name:")
    player2_label.pack()
    
    player2_entry = tk.Entry(top)
    player2_entry.pack()
    
    submit_button = tk.Button(top, text="Submit", command=submit_names)
    submit_button.pack()

def print_scoreboard():
    score_label.config(text="{} (X): {}\n{} (O): {}".format(player1_name, score_board['X'], player2_name, score_board['O']))

root = tk.Tk()
root.title("Tic Tac Toe")

player1_name = "Player X"
player2_name = "Player O"

frame = tk.Frame(root)
frame.pack()

values = [' ' for x in range(9)]
player_pos = {'X':[], 'O':[]}
cur_player = 'X'
score_board = {'X':0, 'O':0}

buttons = []
for i in range(9):
    button = tk.Button(frame, text=str(i+1), font=('Helvetica', '20'), height=3, width=6)
    button.grid(row=i//3, column=i%3)
    button.config(command=lambda button=button: single_game(button))
    buttons.append(button)

reset_button = tk.Button(root, text="Reset Game", font=('Helvetica', '20'), command=reset_game)
reset_button.pack()

score_label = tk.Label(root, text="", font=('Helvetica', '20'))
score_label.pack()

get_player_names()

root.mainloop()
