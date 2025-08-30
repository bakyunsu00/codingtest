from collections import deque
def validParen(sentences):
    # print(sentences)
    parenStack = deque()
    # parenCount = 0
    results = []
    for sentence in sentences:
        parenStack.clear()
        for char in sentence:
            if char == ")" and len(parenStack) > 0 and parenStack[-1] == "(":
                # parenCount = 1
                parenStack.pop()
            elif char == "]" and len(parenStack) > 0 and parenStack[-1] == "[":
                # parenCount = 1
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


#괄호 판별
#괄호 카운트가 0이면 Yes
#괄호 카운트가 1보다 크고 스택에 남으면 괄호가 남으면 No
#괄호 카운트가 1보다 크고 스택에 남은게 없다면 Yes


#문장 리스트 받기






#문장 리스트 하나씩 처리
#문장에서 괄호 하나 뽑고 스택에 추가
#만약 스택에 괄호가 ) 또는 ]이면 스택에 있는 거 pop 아니면 push