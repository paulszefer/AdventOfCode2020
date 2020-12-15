from helper import *

data = inputFileToList('day_3_input.txt')

lineLength = len(data[0])
tree = '#'

def huggedTree(x, y):
    return data[y][x] == tree

def countTreesHugged(dx, dy):
    treesHugged = 0
    x = 0
    y = 0
    while (y < len(data)):
        x = x if (x < lineLength) else x - lineLength
        treesHugged += 1 if (huggedTree(x, y)) else 0
        x += dx
        y += dy
    return treesHugged

print(countTreesHugged(1, 1) * countTreesHugged(3, 1) * countTreesHugged(5, 1) * countTreesHugged(7, 1) * countTreesHugged(1, 2))

# 958815792