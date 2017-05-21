def printHorizLine():
    print(" ---" * boardSize)

def printVertLine():
    print("|   " * (boardSize + 1))


if __name__=="__main__":
    boardSize = int(input("What size of game board? "))

    for index in range(boardSize):
        printHorizLine()
        printVertLine()
    printHorizLine()
