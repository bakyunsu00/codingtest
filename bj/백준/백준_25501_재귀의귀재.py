'''
문자열을 맨 앞과 맨 뒤가 같은지 확인 후 같으면 다음으로 아니면 0반환
만약 맨 앞과 뒤의 인덱스가 같거나 맨 앞의 인덱스가 맨 뒤의 인덱스보다 크면 1반환
매 번 맨 앞 인덱스+1 맨뒤 인덱스-1
'''

nums = int(input())
testcase_str = []
results = []
for _ in range(nums):
    testcase_str.append(input())

count = 0

def isPalindrome(str,start,end,count):
    if start >= end:

        results.append([1,count])
        return
    elif str[start] != str[end]:

        results.append([0,count])
        return
    else:
        isPalindrome(str,start+1,end-1,count+1)

for str in testcase_str:
    isPalindrome(str,0,len(str)-1,1)

for result in results:
    print(*result)
