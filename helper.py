def inputFileToList(filename):
    with open(filename, 'r') as input_file:
        return list(input_file.read().splitlines())
        
def inputFileToIntList(filename):
    with open(filename, 'r') as input_file:
        return list(map(lambda v: int(v), input_file.read().splitlines()))

def hasSubstring(s, sub):
    return s.find(sub) != -1

def isBetween(value, min, max):
    return value >= min and value <= max

defaultKeyTagSeparator = ':'
def getTagValue(s, tag, separator = defaultKeyTagSeparator):
    start = s.find(tag + separator)
    if (start == -1):
        return ''
    
    start += len(tag + separator)
    end = start + s[start:].find(' ')
    
    return s[start:end]
    
def getTagValueInt(s, tag, separator = defaultKeyTagSeparator):
    try:
        return int(getTagValue(s, tag, separator))
    except:
        return -1

def isHex(s):
    return all(c in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f') for c in s)