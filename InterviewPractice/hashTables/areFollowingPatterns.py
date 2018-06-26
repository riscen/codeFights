def areFollowingPatterns(strings, patterns):
    stringPatterns = []
    for i in range(len(strings)):
        for stringPattern in stringPatterns:
            if (strings[i] == stringPattern[0] and patterns[i] != stringPattern[1]) or (strings[i] != stringPattern[0] and patterns[i] == stringPattern[1]):
                return False
            elif strings[i] == stringPattern[0] and patterns[i] == stringPattern[1]:
                break
        stringPatterns.append([strings[i], patterns[i]])        
    return True
