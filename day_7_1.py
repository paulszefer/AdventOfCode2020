from helper import *

data = inputFileToList('day_7_input.txt')

def bagCanContainGold(bags, outerBag):
    foundGold = False
    for innerBag in bags[outerBag]:
        if (innerBag == "shiny gold"):
            foundGold = True
            break
        else:
            if (bagCanContainGold(bags, innerBag)):
                foundGold = True
                break
    if (foundGold):
        bags[outerBag] = [ "shiny gold" ]
    return foundGold

bags = { }

for rule in data:
    outerBag, discard, temp = rule.partition(' bags contain ')
    for subrule in temp.split(', '):
        innerBag, discard, discard = subrule.partition(' bag')
        discard, discard, innerBag = innerBag.partition(' ')
        li = bags.get(outerBag, {})
        li[innerBag] = {}
        bags[outerBag] = li
        bags[innerBag] = bags.get(innerBag, {})

bagCount = 0

for outerBag in bags.keys():
    bagCount += 1 if bagCanContainGold(bags, outerBag) else 0

print(bagCount)

#