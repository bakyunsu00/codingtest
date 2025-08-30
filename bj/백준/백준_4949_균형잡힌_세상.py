from collections import deque
def validParen(sentences):
    # print(sentences)
    parenStack = deque()

    results = []
    for sentence in sentences:
        parenStack.clear()
        for char in sentence:
            if char == ")" and len(parenStack) > 0 and parenStack[-1] == "(":

                parenStack.pop()
            elif char == "]" and len(parenStack) > 0 and parenStack[-1] == "[":

                parenStack.pop()
            elif char == "(" or char == "[":
                parenStack.append(char)
        if not parenStack:

            results.append("Yes")
        else:
            results.append("No")
    for _ in results:
        print(_)
#입력 받아 하나씩 뽑기, .점으로 나눠서 리스트에 저장 후 뽑기
sentences = []
charCount = 0
char = ""
while charCount == 0:
    char = input()
    if char == ".":
        charCount = 1
        break
    sentences.append(char.split(".")[0])

validParen(sentences)






