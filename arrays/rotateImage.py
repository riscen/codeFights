def rotateImage(a):
    rows = len(a)
    columns = len(a[0])
    a_rotated = [[0 for r in range(rows)] for c in range(columns)]
    for i in range(rows): 
        for j in range(columns): 
            a_rotated[j][columns-i-1] = a[i][j]
    return a_rotated
