from helper import *

data = inputFileToIntList('day_1_input.txt')
record = {}

for value in data:
    record[2020 - value] = record.get(2020 - value, 0) + 1

for value in data:
    if (record.get(value, 0) > 0):
        print(value * (2020 - value))

# 996075