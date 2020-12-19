from helper import *

def solution():
    data = inputFileToList('day_8_input.txt')
    data.append('end +0')

    flipOperationIndex = 0

    while (flipOperationIndex < 1000):
        visited = {}
        accumulator = 0
        index = 0
        operationIndex = 0

        while (visited.get(index) != True):
            visited[index] = True
            operation, argument = data[index].split(" ")
            if (index == flipOperationIndex and (operation == "jmp" or operation == "nop")):
                operation = "jmp" if (operation == "nop") else "nop"
            if (operation == "end"):
                return accumulator
            elif (operation == "jmp"):
                index += int(argument)
            else:
                if (operation == "acc"):
                    accumulator += int(argument)
                index += 1

            operationIndex += 1
        
        flipOperationIndex += 1
    
    return "YOU FAILED!"

print(solution())

# 