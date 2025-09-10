'''
8
table
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''


table = [[1, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [1, 0, 0, 0, 1, 1, 1, 1],
         [0, 1, 0, 0, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1, 1, 1]]

x,y = 0,0
n = 8
white = 0
black = 0

def solve(x,y,n):
    global white
    global black
    if n == 1:
        if table[x][y] == 0:
            white += 1
        else:
            black += 1
        return


    ok, color = divide(x,y,n)
    if ok:
        if color == 0: white += 1
        else:
            black += 1
    else:
        half = n//2

        # 좌상단 x~n//2, y~n//2
        solve(x,y,half)

    # 우상단 x~n//2, (y+n/2)~n
        solve(x,y+half,half)

    # 좌하단 (x+n/2)~n ,y~(n/2)
        solve(x+half,y,half)

    # 우하단 (x+n/2)~n, (y+n/2)~n
        solve(x+half,y+half,half)




def divide(x,y,n):
    valid = 0

    base = table[x][y]
    for i in range(x,x+n):
        for c in range(y,y+n):
            if table[i][c] != base:
                return False, None
    return True, base
solve(0,0,8)
print(f"화이트:{white}, 블랙:{black}")