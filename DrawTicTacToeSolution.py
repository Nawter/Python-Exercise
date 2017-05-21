# Initialise the game board
gameboard = [(['€']*3) for i in range(3)]

# Variables for input and turn count
rowCol =[0]
turn = 1

# Checks the input is valid
def inputValid(values):
    # Input has two values
    if len(values) !=2:
        print ("Input must be two numbers in format row, col e.g. 1,2")
        return 0
    # Input is a number between 1 and 3 (inclusive)
    try:
        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
            # checks if the position on the board is already filled
            if gameboard[int(values[0])-1][int(values[1])-1] !='€':
                print("Poistion on the board already taken.")
                return 0
            return 1
        else:
            print("Input values must be numbers between 1 and 3 (inclusive)")
            return 0
    except ValueError:
        print ("Input values must be numbers between 1 and 3 (inclusive)")

# Draw the board
def drawBoard(values, player):
    # Changes the value to X or O
    gameboard[int(values[0])-1][int(values[1])-1] = player

    # Print the gameboard
    for row in gameboard:
        print (row)


# Calculate if the game is over (no more '.' or has winner)
def gameOver():
    search = '€'

    # Check win by row
    for i in range(3):
        if len(set(gameboard[i])) == 1:
            if gameboard[i][1] == '€':
                continue
            elif gameboard[i][1] == 'X':
                print ("Game over - Player 1 wins - A")
            else:
                print ("Game over - Player 2 wins")
            return 1

    # Check win by column
    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard [2][i]:
            if gameboard[0][i] == '€':
                continue
            elif gameboard[0][i] == 'X':
                print ("Game over - Player 1 wins - B")
            else:
                print ("Game over - Player 2 wins")
            return 1

    # Check win by diagonal
    for i in range(3):
        if (gameboard[0][0] == gameboard[1][1] == gameboard [2][2]) or (gameboard[0][2] == gameboard[1][1] == gameboard [2][0]):
            if gameboard[1][1] == 'X':
                print ("Game over - Player 1 wins - C")
            elif gameboard[1][1] == 'O':
                print ("Game over - Player 2 wins")
            else:
                return 0
            return 1

    # Check board is full
    for sublist in gameboard:
        if search in sublist:
            return 0

    print("Game over - the board is filled")
    return 1


while not gameOver():
    piece = '€'


    # Player input - checks for input correctness
    while not inputValid(rowCol):
        player = turn % 2
        if player == 0:
            player = 2
            piece = 'O'
        else:
            piece = 'X'
        p1 = input ('Player' + str(player) + 'input: ')
        rowCol = p1.split(",")

    drawBoard(rowCol, piece)

    rowCol =[0]
    turn +=1




if __name__ == '__main__':
    gameOver()
