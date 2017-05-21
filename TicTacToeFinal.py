def drawLine(width, edge, filling):
    print (filling.join([edge] * (width + 1)))

def displayWinner(player):
    if player == 0:
        print("Tie")
    else:
        print("Player " + str(player) + "wins!")

def checkRowWinner(row):
    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    return 0

def getColumn(game, columNumber):
    return [game[x][columNumber] for x in range(3)]

def getRow(game, rowNumber):
    return game[rowNumber]

def checkWinner(game):
    gameSlices = []
    for index in range(3):
        gameSlices.append(getRow(game, index))
        gameSlices.append(getColumn(game, index))
    # checkDiagonals
    downDiagonal = [game[x][x] for x in range(3)]
    upDiagonal = [game[0][2], game[1][1], game[2][0]]
    gameSlices.append(downDiagonal)
    gameSlices.append(upDiagonal)

    for gameSlice in gameSlices:
        winner = checkRowWinner(gameSlice)
        if winner !=0:
            return winner
    return winner

def startGame():
    return [[0,0,0,] for x in range(3)]

def displayGame(game):
    d = {2:"O", 1:"X" , 0:"_"}
    drawLine(3," ", "_")
    for rowNumber in range(3):
        newRow = []
        for columNumber in range(3):
            newRow.append(d[game[rowNumber][columNumber]])
        print("|" + "|".join(newRow) + "|")

def addPiece(game, player, row, column):
    game[row][column] = player
    return game

def checkSpaceEmpty(game, row, column):
    return game[row][column] == 0

def convertInputToCoordinate(userInput):
    return userInput - 1

def switchPlayer(player):
    if player == 1:
        return 2
    else:
        return 1

def moveExist(game):
    for rowNumber in range(3):
        for columNumber in range(3):
            if game[rowNumber][columNumber] == 0:
                return True
    return False

if __name__ == '__main__':
    game = startGame()
    displayGame(game)
    player = 1
    winner = 0 # The winner is not yet defined.

    # Infinite loop
    while winner == 0 and moveExist(game):
        print("Current player:" + str(player))
        available = False
        while not available:
            row = convertInputToCoordinate(int(input("Which row ? (start with 1) ")))
            column = convertInputToCoordinate(int(input("Which column ?(start with 1) ")))
            available = checkSpaceEmpty(game, row, column)
        game = addPiece(game, player, row, column)
        displayGame(game)
        player = switchPlayer(player)
        winner = checkWinner(game)
    displayWinner(winner)
