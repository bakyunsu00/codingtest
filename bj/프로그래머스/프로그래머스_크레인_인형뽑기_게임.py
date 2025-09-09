# 테이블 배열의 인형들은 모두 스택  5x5 ~ 30x30                // 2중 for문으로 각 값들 스택에 push
# 반출구 배열에 인형도 모두 스택                   // 반출구 스택 만듦
# 같은 인형이 2개 모이면 터짐 => 값 저장 후 리턴    // 인형을 넣을 때 리턴 배열 스택 peak와 비교후 POP 및 값++
# 인형의 종류는 숫자로 표현 ~100, 0은 비어있음    //
# 비어 있는 곳에서 크레인이 작동하면 아무일도 없음    // 테이블 스택을 pop 하기 전에 0 이면 그냥 countinue
# 입력값 move는 각 테이블의 위치로 크레인이 이동해서 인형을 뽑음
from collections import deque

stack = deque()



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
''' 
[00000]
[00103]
[02501]
[42442]
[35131]
'''
move = [1,5,3,5,1,2,1,4]
table = [[0] * len(board) for _ in range(len(board)) ]
# print(table)
# print(len(table))
for _ in range(len(board)):
    for i in range(len(board)):
        table[i][_] = board[-_-1][i]

# print(table)
count = 0
result = deque()

for location in move:
    if table[location-1]:
        while table[location-1][-1] == 0:
            select = table[location-1].pop()
        select = table[location-1].pop()
        if select != 0 :
            result.append(select) #추가
            # if result:
                # if result[-1] != select:
                # result.append(select)
                # elif result[-1] != select:
                #     result.pop()
                #     count += 1
            # else:
            #     result.append(select)
stack = deque()
while result:
    select = result.popleft()
    if stack:
        if stack[-1] == select:
            stack.pop()
            count += 2
        elif stack[-1] != select:
            stack.append(select)
    else:
        stack.append(select)

# print(result)
print(count)

# 제출 답안


# from collections import deque
#
# def solution(board, moves):
#
#     table = [[0] * len(board) for _ in range(len(board)) ]
#     # print(table)
#     # print(len(table))
#     for _ in range(len(board)):
#         for i in range(len(board)):
#             table[i][_] = board[-_-1][i]
#
#     # print(table)
#     count = 0
#     result = deque()
#
#     for location in moves:
#         if table[location-1]:
#             while table[location-1][-1] == 0:
#                 select = table[location-1].pop()
#             select = table[location-1].pop()
#             if select != 0 :
#                 result.append(select) #추가
#                 # if result:
#                 # if result[-1] != select:
#                 # result.append(select)
#                 # elif result[-1] != select:
#                 #     result.pop()
#                 #     count += 1
#                 # else:
#                 #     result.append(select)
#     stack = deque()
#     while result:
#         select = result.popleft()
#         if stack:
#             if stack[-1] == select:
#                 stack.pop()
#                 count += 2
#             elif stack[-1] != select:
#                 stack.append(select)
#         else:
#             stack.append(select)
#
#     # print(result)
#
#
#
#
#     answer = count
#     return answer