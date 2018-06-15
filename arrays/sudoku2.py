def sudoku2(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != '.':
                row = (i) - (i)%3
                column = (j) - (j)%3
                c = grid[i][j]
                for k in range(row, row+3):
                    for l in range(column, column+3):
                        if k != i and l != j and c == grid[k][l]:
                            return False
                        elif ((k-row)*3+(l-column) != i and c == grid[(k-row)*3+(l-column)][j]) or ((k-row)*3+(l-column) != j and c == grid[i][(k-row)*3+(l-column)]):
                            return False
    return True
