def firstDuplicate(a):
    a_len = len(a)
    if a_len == len(set(a)):
        return -1
    a_set = set()
    for i in range(a_len):
        if a[i] in a_set or a_set.add(a[i]):
            break
    return a[i]
                
