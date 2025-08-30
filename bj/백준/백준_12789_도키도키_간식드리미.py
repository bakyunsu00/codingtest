from collections import deque


infrontOfMe = int(input())
waitingList = deque((map(int, input().split(" "))))


sideWating = deque()


#4 5 1 2 3
watingCounts = range(1 , infrontOfMe+1)

for watingCount in watingCounts:
    while True:
        if waitingList:
            pickedPerson = waitingList.popleft()
            if len(sideWating) != 0 and sideWating[-1] == watingCount:
                sideWating.pop()
                waitingList.appendleft(pickedPerson)
                break
            elif pickedPerson != watingCount:
                sideWating.append(pickedPerson)
            elif pickedPerson == watingCount:
                break
        elif len(sideWating) != 0 and sideWating[-1] == watingCount:
                sideWating.pop()
                break
        else:
            break







if len(sideWating) == 0 and len(waitingList) == 0:
    print("Nice")
else:
    print("Sad")

