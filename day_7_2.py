from helper import *

data = inputFileToList('day_7_input.txt')

def getInnerBagCount(bags, outerBag):
    tempCount = 0
    for innerBag in bags[outerBag].items():
        tempCount += innerBag[1] * getInnerBagCount(bags, innerBag[0])
        tempCount += innerBag[1]
    return tempCount

bags = { }

for rule in data:
    outerBag, discard, temp = rule.partition(' bags contain ')
    for subrule in temp.split(', '):
        innerBag, discard, discard = subrule.partition(' bag')
        count, discard, innerBag = innerBag.partition(' ')
        innerBags = bags.get(outerBag, {})
        innerBags[innerBag] = 0 if (count == "no") else int(count)
        bags[outerBag] = innerBags
        bags[innerBag] = bags.get(innerBag, {})


bagCount = getInnerBagCount(bags, "shiny gold")

print(bagCount)

#