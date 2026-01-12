#!/usr/bin/python3
def print_board(board):
    """
    Displays the current state of the board.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    """
    Checks if there is a winner.

    Parameters:
        board (list): 3x3 tic-tac-toe board

    Returns:
        str | None: 'X' or 'O' if there is a winner, otherwise None
    """
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
	# Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_draw(board):
    """
    Checks if the game is a draw.

    Returns:
        bool: True if the board is full and no winner, otherwise False
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function that runs the Tic-Tac-Toe game.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
            continue
        
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of bounds. Try again.\n")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
