from helper import *

data = inputFileToList('day_4_input.txt')

def hasValidBirthYear(passport):
    birthYear = getTagValueInt(passport, 'byr')
    return isBetween(birthYear, 1920, 2002)

def hasValidIssueYear(passport):
    issueYear = getTagValueInt(passport, 'iyr')
    return isBetween(issueYear, 2010, 2020)

def hasValidExpirationYear(passport):
    expirationYear = getTagValueInt(passport, 'eyr')
    return isBetween(expirationYear, 2020, 2030)

def hasValidHeight(passport):
    heightValue = getTagValue(passport, 'hgt')
    if (heightValue == ''):
        return False
    height = int(heightValue[0:-2])
    heightUnit = heightValue[-2:]
    return heightUnit == 'cm' and isBetween(height, 150, 193) or heightUnit == 'in' and isBetween(height, 59, 76)

def hasValidHairColour(passport):
    hairColour = getTagValue(passport, 'hcl')
    if (hairColour == ''):
        return False
    return hairColour[0] =='#' and isHex(hairColour[1:])

def hasValidEyeColour(passport):
    return getTagValue(passport, 'ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def hasValidPassportID(passport):
    passportID = getTagValue(passport, 'pid')
    return len(passportID) == 9 and passportID.isnumeric()

def isValidPassport(passport):
    return (hasValidBirthYear(passport)
        and hasValidIssueYear(passport)
        and hasValidExpirationYear(passport)
        and hasValidHeight(passport)
        and hasValidHairColour(passport)
        and hasValidEyeColour(passport)
        and hasValidPassportID(passport))

validPassports = 0
currentLine = ''

for line in data:
    currentLine += line + ' '
    if (line == ''):
        if (isValidPassport(currentLine)):
            validPassports += 1
        currentLine = ''

print(validPassports)

# 137