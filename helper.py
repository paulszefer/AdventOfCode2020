def inputFileToList(filename):
    with open(filename, 'r') as input_file:
        return list(input_file.read().splitlines())
        
def inputFileToIntList(filename):
    with open(filename, 'r') as input_file:
        return list(map(lambda v: int(v), input_file.read().splitlines()))