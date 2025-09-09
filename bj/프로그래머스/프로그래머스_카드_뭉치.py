from collections import deque
# 카드 뭉치 1또는 2의 맨 왼쪽이 골의 맨 왼쪽과 같으면 푸시
# 만약 둘다 같지 않으면 No
# 카드 뭉치 1과 2의 값이 비어있고 골의 문장을 다 만들었으면 Yes

from collections import deque
# 카드 뭉치 1또는 2의 맨 왼쪽이 골의 맨 왼쪽과 같으면 푸시
# 만약 둘다 같지 않으면 No
# 카드 뭉치 1과 2의 값이 비어있고 골의 문장을 다 만들었으면 Yes

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    side = deque()
    goal = deque(goal)
    goal_temp = deque(goal)
    answer = ""

    while goal_temp:
        if cards1 and (cards1[0] == goal_temp[0]):
            select = cards1.popleft()
            goal_temp.popleft()
            side.append(select)
        elif cards2 and (cards2[0] == goal_temp[0]):
            select =  cards2.popleft()
            goal_temp.popleft()
            side.append(select)
        elif (not cards1 and (cards2[0] != goal_temp[0])) or (not cards2 and (cards1[0] != goal_temp[0])) :
            answer = "No"
            break

        elif (cards1[0] != goal_temp[0]) and (cards2[0] != goal_temp[0]):
            answer = "No"
            break
    if side == goal:
        answer = "Yes"
    elif side != goal:
        answer = "No"




    return answer
a=["i", "drink", "wateㄴr"]
b=["want", "to"]
c=["i", "want", "to", "drink", "water"]

print(solution(a,b,c))