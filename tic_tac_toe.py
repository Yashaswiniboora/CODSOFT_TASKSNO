import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(board[a] == board[b] == board[c] == player
               for a, b, c in wins)

def minimax(is_maximizing):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best

def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


print("Tic-Tac-Toe AI")
print("You = X | AI = O")
print("Positions are 1 to 9")

while True:

    print_board()

    try:
        position = int(input("Enter your position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move! Try again.")
            continue

        board[position] = "X"

    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if winner("X"):
        print_board()
        print("You win!")
        break

    if " " not in board:
        print_board()
        print("It's a draw!")
        break

    ai_move()

    if winner("O"):
        print_board()
        print("AI wins!")
        break