from helper import *

data = inputFileToList('day_6_input.txt')
data.append('')

def getAnswerCount(answers, memberCount):
    answerRecord = { }
    for answer in answers:
        answerRecord[answer] = answerRecord.get(answer, 0) + 1
    return sum(value == memberCount for value in answerRecord.values())
    
answerCount = 0
memberCount = 0
currentLine = ''

for line in data:
    currentLine += line
    if (line == ''):
        answerCount += getAnswerCount(currentLine, memberCount)
        currentLine = ''
        memberCount = 0
    else:
        memberCount += 1

print(answerCount)

# 3202