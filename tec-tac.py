import random

# Initialize the tic-tac-toe board
board = [' '] * 9

# Define winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Function to display the current board state
def display_board(board):
    print("  {} | {} | {}".format(board[0], board[1], board[2]))
    print(" -----------")
    print("  {} | {} | {}".format(board[3], board[4], board[5]))
    print(" -----------")
    print("  {} | {} | {}".format(board[6], board[7], board[8]))

# Function to check if the game is over
def check_game_over(board):
    # Check for winning combinations
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]] # Return the winner

    # Check for a tie
    if ' ' not in board:
        return 'Tie'

    # Game is not over yet
    return None

# Main game loop
def play_game():
    # Initial display of the board
    display_board(board)

    # Computer makes the first move by placing 'X' in the middle
    board[4] = 'X'

    while True:
        # User's turn
        while True:
            user_move = input("Enter your move (1-9): ")
            if user_move.isdigit() and 1 <= int(user_move) <= 9 and board[int(user_move) - 1] == ' ':
                board[int(user_move) - 1] = 'O'
                break
            else:
                print("Invalid move. Try again.")

        # Check if the game is over after user's move
        game_over = check_game_over(board)
        if game_over:
            break

        # Computer's turn
        while True:
            computer_move = random.randint(0, 8)
            if board[computer_move] == ' ':
                board[computer_move] = 'X'
                break

        # Check if the game is over after computer's move
        game_over = check_game_over(board)
        if game_over:
            break

        # Display the current board state
        display_board(board)

    # Display the final board state
    display_board(board)

    # Print the game result
    if game_over == 'Tie':
        print("It's a tie!")
    elif game_over == 'O':
        print("Congratulations! You win!")
    else:
        print("Computer wins!")

# Start the game
play_game()
