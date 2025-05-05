def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Checks if there is a winner on the board."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"  # Switch player
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print_board(board)
    print("Player " + ("O" if player == "X" else "X") + " wins!")  # Correct winner

tic_tac_toe()
