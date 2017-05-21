import numpy

def checkGrid(grid):
    # Rows
    for x in range(0,3):
        row = set([grid[x][0],grid[x][1],grid[x][2]])
        if len(row) == 1 and grid[x][0] != 0:
            return grid[x][0]

    # Cols
    for x in range(0,3):
        col = set([grid[0][x],grid[1][x],grid[2][x]])
        if len(col) == 1 and grid[0][x] != 0:
            return grid[0][x]

    # Diagonals
    dig1 = set([grid[0][0],grid[1][1],grid[2][2]])
    dig2 = set([grid[0][0],grid[2][0],grid[0][2]])
    if len(dig1) == 1 or len(dig2) == 1 and grid[1][1] != 0:
        return grid[1][1]

    return 0    
winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(checkGrid(no_winner))
