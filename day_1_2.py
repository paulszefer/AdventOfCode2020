from helper import *

data = inputFileToIntList('day_1_input.txt')

for i in range(0, len(data) - 2):
    for j in range(0, len(data) - 1):
        for k in range(0, len(data)):
            if (data[i] + data[j] + data[k] == 2020):
                print(data[i] * data[j] * data[k])

# 51810360