def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check for a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return " " not in board

# Function to handle the game logic
def play_game():
    # Initial empty board
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! The position is already taken or out of range.")
            continue
        
        # Make the move
        board[move] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    play_game()
