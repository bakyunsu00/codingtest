
n = int(input())
table = [n * [] for a in range(n)]
for _ in range(n):
    str = input()
    for i in str:
        table[_].append(int(i))


'''
up = x-1, y
down = x+1 ,y
left = x, y-1
right = x, y+1
'''


visited_table = [n * [False]for _ in range(n)]
result_count =[]


nx = [-1,1,0,0]
ny = [0,0,+1,-1]


def solve():




    for x in range(n):
        for y in range(n):
            if visited_table[x][y] == False and table[x][y] != 0:
                count_num = dfs(x,y)
                if count_num != 0:
                    result_count.append(count_num)

def is_visited(x,y):
    if visited_table[x][y]:
        return True
    else:
        return False

def dfs(x,y):
    count = 0
    dx = x
    dy = y
    num = table[x][y]
    v = is_visited(x,y)
    if not v:
        visited_table[x][y] = True
        if num == 1:
            count += 1

        else:

            return count
        for i in range(4):
            dx = x+nx[i]
            dy = y+ny[i]
            if (dx >= 0 and dx < n) and (dy >= 0 and dy < n) and (visited_table[dx][dy] == False):
                count = count + dfs(dx,dy)   #여기서 count를 누적하지 않아서 시간 허비


    return count

solve()
print(len(result_count))
result_count.sort()  # 오름차순으로 출력이라는 내용을 지나쳐서 30분 허비
for result in result_count:
    print(result)













