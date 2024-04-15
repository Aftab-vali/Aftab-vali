import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def on_click(row, col):
    global current_player

    # Check if the cell is empty
    if game_board[row][col] == "":
        # Update the game board with the current player's symbol
        game_board[row][col] = current_player
        # Update the button text to display the current player's symbol
        buttons[row][col].config(text=current_player)

        # Check if the current player has won
        if check_winner(current_player):
            # Display winner message
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            root.quit()
        # Check if the game has ended in a draw
        elif all(all(cell != "" for cell in row) for row in game_board):
            # Display draw message
            messagebox.showinfo("Draw", "It's a draw!")
            root.quit()

        # Switch to the other player for the next turn
        current_player = "X" if current_player == "O" else "O"

# Function to check if a player has won
def check_winner(player):
    # Check rows and columns
    for i in range(3):
        if all(game_board[i][j] == player for j in range(6)) or all(game_board[j][i] == player for j in range(6)):
            return True

    # Check diagonals
    if all(game_board[i][i] == player for i in range(6)) or all(game_board[i][2 - i] == player for i in range(6)):
        return True

    return False

# Initialize Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize current player and game board
current_player = "X"
game_board = [["" for _ in range(6)] for _ in range(6)]

# Create buttons for the Tic-Tac-Toe grid
buttons = [[None for _ in range(6)] for _ in range(6)]
for i in range(3):
    for j in range(3):
        # Create buttons and assign command to on_click function with row and col parameters
        buttons[i][j] = tk.Button(root, text="", width=10, height=4,
                                  font=("Arial", 20),
                                  command=lambda row=i, col=j: on_click(row, col))
        # Place buttons in the grid
        buttons[i][j].grid(row=i, column=j)

# Start Tkinter event loop
root.mainloop()
