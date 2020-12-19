from helper import *

data = inputFileToList('day_5_input.txt')

def upper(min, max):
    return (max + min) // 2 + 1, max

def lower(min, max):
    return min, (max + min) // 2

partitionOperations = { 'F': lower, 'B': upper, 'L': lower, 'R': upper }

def getRow(bsp):
    min = 0
    max = 127
    for partitionKey in bsp:
        min, max = partitionOperations[partitionKey](min, max)
    return min

def getCol(bsp):
    min = 0
    max = 7
    for partitionKey in bsp:
        min, max = partitionOperations[partitionKey](min, max)
    return min

def getSeatInfo(boardingPass):
    row = getRow(boardingPass[:7])
    col = getCol(boardingPass[7:])
    seatID = row * 8 + col

    return row, col, seatID

seats = { }

for boardingPass in data:
    row, col, seatID = getSeatInfo(boardingPass)
    seats[seatID] = False

for i in range(0, 1024):
    if (seats.get(i, True) == True):
        print(i)

# 629