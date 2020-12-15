from helper import *

data = inputFileToList('day_2_input.txt')

validPasswords = 0

# example of record:
# 1-4 z: zsgz
for record in data:
    minCount, temp = record.split('-', 1)
    maxCount, temp = temp.split(' ', 1)
    char, temp = temp.split(': ', 1)
    password = temp

    charCount = len(password) - len(password.replace(char, ''))
    if (charCount >= int(minCount) and charCount <= int(maxCount)):
        validPasswords += 1

print(validPasswords)

# 625