from helper import *

def solution():
    data = inputFileToList('day_8_input.txt')

    visited = {}
    accumulator = 0
    index = 0

    while (visited.get(index) != True):
        visited[index] = True
        operation, argument = data[index].split(" ")
        if (operation == "jmp"):
            index += int(argument)
        else:
            if (operation == "acc"):
                accumulator += int(argument)
            index += 1
    
    return accumulator

print(solution())

# 254