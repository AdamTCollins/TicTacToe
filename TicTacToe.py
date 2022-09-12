
board = [" " for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == " "

# Printing Board
def printBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

# Checking if there's a winner
def isWinner(bo, le):
    # Horizontals: 1,2,3 and 4,5,6 and 7,8,9
    # Verticles: 1,4,7 and 3,6,9
    # Diagonals: 1,5,9 and 3,5,7
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

# User input - Ensures valid input
def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move) 
            if move > 0 and move < 10:
                if spaceIsFree(move):
                     run = False
                     insertLetter("X", move)
                else:
                    print("Sorry, this space is occupied! ")
            else:
                print("Please type a number within the range! ")
        except:
            print("Please type a number! ")

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    
    # Checks if Computer can win, then checks if player can win
    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner (boardCopy, let):
                move = i
                return move
    

    # Checks if the computer can place a move in the middle
    if 5 in possibleMoves:
        move = 5
        return move

    # Checks if the computer can place a move in a corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
        
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    

    # Checks if the computer can place a move in an edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
        
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move

# Generating computer move
def selectRandom(li):
    import random
    ln = len(li) 
    r = random.randrange(0, ln)
    return li[r]

# Checking if board is full
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
 
# Checking who wins and printing outcomes
def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull (board)):
        if not (isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("O's have won the game!")
            break 

        if not (isWinner(board, "X")):
            move = compMove()
            if move == 0:
                print("It's a draw!")
            else:
                insertLetter("O", move)
                print("Computer placed an 'O' in position", move , ":")
                printBoard(board)
        else:
            print("X's have won the game!")
            break   

main()

# A
while True:
    answer = input("Do you want to play again? If so, type yes: ")
    if answer.lower() == ("yes"):
        board = [" " for x in range(10)]
        print("-----------------------------------")
        main()
    else:
        break