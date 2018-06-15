def firstNotRepeatingCharacter(s):
    s_set = set()
    i = 0
    while i < len(s):
        c = s[i]
        if c in s_set:
            s = s.replace(c, "")
            s_set = set()
            i = -1
        else:
            s_set.add(c)
        i += 1
    if len(s) == 0:
        return '_'
    return s[0]