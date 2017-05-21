import numpy

game = [
[2,1,1],
[1,2,0],
[1,2,2]]

setRow = ()
setCol = ()

def rowMatch(game):
    for i in range(3):
        setRow = set(game[i])
        if len(setRow) == 1 and game[i][0] !=0:
            return game[i][0]
    return 0

def colMatch(game):
    trans = numpy.transpose(game)
    for i in range(3):
        setRow = set(trans[i])
        if len(setRow) == 1 and trans[i][0] !=0:
            return list(setRow)[0]
    return 0

def diagonalMatch(game):
    if game[1][1] !=0:
        if game[1][1] == game[0][0] == game[2][2]:
            return game[1][1]
        elif game[1][1] == game[0][2] == game[2][0]:
            return game[1][1]
    return 0

if rowMatch(game) > 0:
    print(str(rowMatch(game)) + str(" row wins!"))
if colMatch(game) > 0:
    print(str(colMatch(game)) + str(" col wins!"))
if diagonalMatch(game) > 0:
    print(str(diagonalMatch(game)) + str(" diagonal wins!"))
