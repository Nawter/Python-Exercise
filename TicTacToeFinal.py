def drawLine(width, edge, filling):
    print("drawLine" + width + "-"+ edge + "-"+ filling +"-")

def displayWinner(player):
    print("displayWinner" + player)

def checkRowWinner(row):
    print("checkRowWinner" + row)

def getColumn(game, columNumber):
    print("getColumn" + game + "-" + columNumber)

def getRow(game, rowNumber):
    print("getRow" + game + "-" + rowNumber)

def checkWinner(game):
    print("checkWinner" + game)

def startGame():
    print("startGame")
    return [[0,0,0,] for x in range(3)]
    
def displayGame(game):
    print("displayGame" + "-" + game)

def addPiece(game, player, row, column):
    print("addPiece" + "-"+ game + "-" + player + "-" + row + "-" + column + "-")

def checkSpaceEmpty(game, row, column):
    print("checkSpaceEmpty" + "-"+ game + "-" + row + "-" + column + "-")

def convertInputToCoordinate(userInput):
    print("convertInputToCoordinate" + "-" + userInput)

def switchPlayer(player):
    print("switchPlayer" + "-" + player)

def moveExist(game):
    print("moveExist" + "-"+ game)

if __name__ == '__main__':
    game = startGame()
    displayGame(game)
    player = 1
    winner = 0 # The winner is not yet defined.

    # Infinite loop
    while winnner == 0 and moveExist(game):
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
