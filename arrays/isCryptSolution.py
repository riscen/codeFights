def isCryptSolution(crypt, solution):
    numbers = []
    for word in crypt:
        digits = ''
        for i in range(len(word)):
            digit = getDigit(word[i], solution)
            if i == 0 and i+1 < len(word)  and digit == '0':
                return False
            digits = digits + digit
            
        numbers.append(digits)
    return int(numbers[0])+int(numbers[1]) == int(numbers[2])
            
            
def getDigit(letter, matrix):
    for array in matrix:
        if letter == array[0]:
            return array[1]
    return null
        
