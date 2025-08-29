from collections import deque


def isValid(parens):
    parens = parens
    parenStack = deque()

    for current in parens:
        # print("current = " + current)

        if current == ")" and len(parenStack) > 0 and parenStack[-1] == "(":
            # print("current = " + parenStack[-1])
            parenStack.pop()
        else:
            parenStack.append(current)
            # print(parenStack)
    return parenStack





parenStringsList = []
num = int(input())
for i in range(num):
    parenStrings = input()
    parenStringsList.append(parenStrings)

for parenString in parenStringsList:
    if not (isValid(parenString)):
        print("YES")
    else:
        print("NO")

