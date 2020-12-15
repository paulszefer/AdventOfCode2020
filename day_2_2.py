from helper import *

data = inputFileToList('day_2_input.txt')

validPasswords = 0

# example of record:
# 1-4 z: zsgz
for record in data:
    pos1, temp = record.split('-', 1)
    pos2, temp = temp.split(' ', 1)
    char, temp = temp.split(': ', 1)
    password = temp

    if (len((password[int(pos1) - 1] + password[int(pos2) - 1]).replace(char, '')) == 1):
        validPasswords += 1

print(validPasswords)

# 391