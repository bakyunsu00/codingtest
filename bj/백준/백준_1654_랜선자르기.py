# 문제 제한시간 내 풀이 실패
#start/end 를 갱신하며 범위를 좁혀야 하는데 계속 start/mid/end 를 좁히는 불필요한 코드를 작성함
#start:mid, mid,end 로 범위를 좁힐 때 mid는 이미 확인 한 값으로 +-로 제외했어야 함
#mid는 start+end//2 하면 되는데 len(range(start,end))//2 로 리스트를 만들어 진행함

N,K = list(map(int,input().split()))
lan_length = []
result = []
for _ in range(N):
    lan_length.append(int(input()))

lan_length.sort()
leng = lan_length[-1]
num = 0
end = lan_length[-1]
start = 1
mid = (start+end)//2

while start <= end:
    num =0
    mid = (start+end)//2
    for lan in lan_length:
        num = num+(lan//mid)
    if num < K:
        end = mid-1
    elif num >= K:
        result.append(mid)
        start = mid+1



result.sort()
print(result[-1])




  
