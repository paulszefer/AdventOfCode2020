from helper import *

data = inputFileToList('day_3_input.txt')

lineLength = len(data[0])
tree = '#'
treesHugged = 0

def huggedTree(x, y):
    return data[y][x] == tree

x = 0
y = 0
while (y < len(data)):
    x = x if (x < lineLength) else x - lineLength
    treesHugged += 1 if (huggedTree(x, y)) else 0
    x += 3
    y += 1

print(treesHugged)

# 282