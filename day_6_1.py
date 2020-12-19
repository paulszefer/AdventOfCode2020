from helper import *

data = inputFileToList('day_6_input.txt')
data.append('')

def getAnswerCount(answers):
    answerRecord = { }
    for answer in answers:
        answerRecord[answer] = True
    return len(answerRecord.keys())

answerCount = 0
currentLine = ''

for line in data:
    currentLine += line
    if (line == ''):
        answerCount += getAnswerCount(currentLine)
        currentLine = ''

print(answerCount)

# 6633