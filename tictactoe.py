import random

board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-"] 

currentplayer = "x"
winner = None 
gameRunning = True 

# Printing the game board 
def printBoard(board): 
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------") 
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8]) 

# Take the player input 
def playerInput(board):  
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": 
        board[inp-1] = currentplayer
    else: 
        print("Oops, that spot is already taken!")

# Check for the win or tie 
def checkHorizontle(board): 
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-": 
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-": 
        winner = board[3] 
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6] 
        return True 
    return False

def checkRow(board): 
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-": 
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-": 
        winner = board[2]
        return True 
    return False

def checkDiag(board): 
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2] 
        return True 
    return False

def checkTie(board): 
    global gameRunning
    if "-" not in board: 
        printBoard(board) 
        print("It is a tie!") 
        gameRunning = False 

def checkWin(): 
    if checkDiag(board) or checkHorizontle(board) or checkRow(board): 
        printBoard(board)
        print(f"The winner is {winner}") 
        global gameRunning
        gameRunning = False

# Switch the player 
def switchPlayer(): 
    global currentplayer 
    if currentplayer == "x": 
        currentplayer = "o"
    else: 
        currentplayer = "x" 

# Computer move
def computer(board):
    while currentplayer == "o" and gameRunning: 
        position = random.randint(0, 8) 
        if board[position] == "-": 
            board[position] = "o"
            switchPlayer()

# Game loop
while gameRunning: 
    printBoard(board) 
    playerInput(board)
    checkWin()
    checkTie(board) 
    switchPlayer() 
    computer(board)
    checkWin()
    checkTie(board)


    


