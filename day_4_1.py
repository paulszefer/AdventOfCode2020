from helper import *

data = inputFileToList('day_4_input.txt')

def isValidPassport(passport):
    return (hasSubstring(passport, 'byr:') 
        and hasSubstring(passport, 'iyr:') 
        and hasSubstring(passport, 'eyr:') 
        and hasSubstring(passport, 'hgt:') 
        and hasSubstring(passport, 'hcl:') 
        and hasSubstring(passport, 'ecl:') 
        and hasSubstring(passport, 'pid:'))

validPassports = 0
passport = ''

for line in data:
    passport += line
    if (line == ''):
        if (isValidPassport(passport)):
            validPassports += 1
        passport = ''

print(validPassports)

# 202