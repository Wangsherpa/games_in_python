##############################################
###########_______PROJECT-1_______############
################| CONNECT 4 |#################
##############################################

import sys
from termcolor import colored, cprint

# draw a board
def drawBoard(field):
    color = 'black'
    for row in range(11):
        if row % 2 == 0:
            practicalRow = int(row/2)
            for column in range(13):
                if column % 2 == 0:
                    practicalColumn = int(column/2)
                    if field[practicalColumn][practicalRow] == 'X':
                        color = 'red'
                    else:
                        color = 'yellow'
                    if column == 12:
                        cprint(field[practicalColumn][practicalRow], color, attrs=['bold'], file=sys.stderr)
                    else:
                        cprint(field[practicalColumn][practicalRow], color, attrs=['bold'], file=sys.stderr, end='')
                else:
                    cprint("|", 'blue', end="")
        else:
            cprint("--------------", 'blue')

# check diagonal results
def checkDiag(currentField, mark, i, j):
    if currentField[i][j] == mark and currentField[i+1][j-1] == mark and currentField[i+2][j-2] == mark and currentField[i+3][j-3] == mark:
        return True
    if j < 3:
        if currentField[i][j] == mark and currentField[i+1][j+1] == mark and currentField[i+2][j+2] == mark and currentField[i+3][j+3] == mark:
            return True

    return False

# Winning Condition
def checkResult(field, mark):
    # Check vertical result
    i, j, k, l = 0, 1, 2, 3
    for row in field:
        for i in range(3):
            if row[i] == mark and row[j+i] == mark and row[k+i] == mark and row[l+i] == mark:
                return True

    # check horizontal result
    for j in range(6):
        for i in range(4):
            if field[i][j] == mark and field[i+1][j] == mark and field[i+2][j] == mark and field[i+3][j] == mark:
                return True
    
    # check diagonal result
    for i in range(4):
        for j in range(0, 6):
            if checkDiag(field, mark, i, j):
                return True
            
    return False

currentField = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ']
]

# call drawBoard
drawBoard(currentField)

Player = 1
totalEntry = 0
while True:
    if Player == 1:
        cprint("Player turn: 1", "red")
    else:
        cprint("Player turn: 2", "yellow")

    if Player == 1:
        column = int(input("Please enter the column number:(0 t0 6) "))
        if column < 7 and column >=0:
            for i in range(1, 7):
                if currentField[column][-i] == ' ':
                    currentField[column][-i] = 'X'
                    totalEntry += 1
                    Player = 2
                    break
            if totalEntry > 6:
                won = checkResult(currentField, 'X')
                if won:
                    drawBoard(currentField)
                    cprint("\n**** Player 1 won ****", 'green', attrs=['bold'], file=sys.stderr)
                    break
    else:
        column = int(input("Please enter the column number:(0 to 6) "))
        if column < 7 and column >=0:
            for i in range(1, 7):
                if currentField[column][-i] == ' ':
                    currentField[column][-i] = 'O'
                    totalEntry += 1
                    Player = 1
                    break
            if totalEntry > 6:
                won = checkResult(currentField, 'O')
                if won:
                    drawBoard(currentField)
                    cprint("\n**** Player 2 won ****", 'green', attrs=['bold'], file=sys.stderr)
                    break
    
    # show the board
    drawBoard(currentField)

