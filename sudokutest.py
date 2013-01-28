raw = "0 0 0 0 0 0 0 0 0 0 0 8 0 0 0 0 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0"
raw = raw.split()

board = []

for i in range(9):
	board.append([int(k) for k in raw[i * 9 : i * 9 + 9] ])

# BRUTE FORCE
def b(g, x, y):
    
    if y > 8:
    	return 1
    
    v = g[x][y]
    n = (x+1)%9
    z = (x+1)/9

    if v == 0:
        s = set()
        for i in range(9):
            s.add(g[x][i])
            s.add(g[i][y])
        for i in range(y/3 * 3, y/3 * 3 + 3):
            for j in range(x/3 * 3, x/3 * 3 + 3):
                s.add(g[j][i])
        for i in range(1,10):
            if i not in s:
                g[x][y] = i
                if b(g, n, y + z):
                    return 1
                g[x][y] = 0
                
        return 0
    
    else:
        return b(g, n, y + z)


def sudoku_solve(grid):
    
    b(grid, 0, 0)
    for i in range(9):
    	print " ".join(str(v) for v in grid[i]);


sudoku_solve(board)


