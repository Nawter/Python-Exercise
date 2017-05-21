import sys
def main():
    def showBoard(gameState):
        print ('')
        for row in gameState:
            print([icon(square) for square in row])

    def swapTurn(playerNumber):
        if playerNumber == 1:
            return 2
        elif playerNumber == 2:
            return 1

    def icon(playerNumber):
        if playerNumber == 1:
            return 'O'
        elif playerNumber == 2:
            return 'X'
        else:
            return ' '

    def checkWin(game , w):
        win = False
        if game[0] == [w,w,w] or game[1] == [w,w,w] or game[2] == [w,w,w]:
            win = True
        elif game[0][0] == w and game[1][0] == w and game[2][0] == w:
            win = True
        elif game[0][1] == w and game[1][1] == w and game[2][1] == w:
            win = True
        elif game[0][2] == w and game[1][2] == w and game[2][2] == w:
            win = True
        elif game[0][0] == w and game[1][1] == w and game[2][2] == w:
            win = True
        elif game[0][2] == w and game[1][1] == w and game[2][0] == w:
            win = True
        return win


    print ('***********************')
    print ('welcome to Tic Tac Toe!')
    print ('***********************')
    print ('in turns please enter your desired move coordinates in the following format:')
    print ('row, column')
    print ('for example to mark the top right square, enter: \'1,3\'\n')

    startState = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    gameState = [list(row) for row in startState]
    turn = 1
    gameOn = True

    while gameOn == True:
        try:
            move =[int(value)-1 for value in input('Player %d (%s), [row,col]:' % (turn,icon(turn))).split(',')]
            if gameState[move[0]][move[1]] == ' ':
                gameState[move[0]][move[1]] = turn
                showBoard(gameState)
                if checkWin(gameState,turn) == True:
                    gameOn = False
                    print('++++++++++++++++++++++++++')
                    print('game over! player %d won!' % turn)
                    print('++++++++++++++++++++++++++')
                turn = swapTurn(turn)
            else:
                print('Ilegal move, please try again.')

        except ValueError:
            print ('\nError. please enter your move using correct format:')
            print ('row, column')

        fullSquares = 0
        for square in gameState[0]+gameState[1]+gameState[2]:
            if square == ' ':
                pass
            else:
                fullSquares += 1
        if fullSquares == 9 and gameOn == True:
            gameOn == False
            print('++++++++++++++++++++++++++')
            print('game over! it\'s a draw.....')
            print('++++++++++++++++++++++++++')

        if gameOn == False:
            yn = input('Do you want to play another game[type y for yes or anything else to exit]?\n').lower()
            if yn == 'y':
                gameState = [list(row) for row in startState]
                gameOn = True
            else:
                sys.exit()

if __name__ == '__main__':
    main()
