import sys

input = sys.stdin.readline


N,M,R = map(int,(input().split(" ")))
graph = [[] for _ in range(N+1)]
'''
# 간선 만큼 만들어야 한다고 생각했지만, 생각해보면 이렇게 만드는 이유가 인데스를 정점, 내용을 간선으로 표현하는 건데
당연히 N이 맞는 거였음
'''

for _ in range(M):
    u,v = map(int,(input().split(" ")))
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
stack = [R]
order = 1

while stack:
    node = stack.pop()
    if visited[node] == 0:
        visited[node] = order
        order += 1
        for nextnode in sorted(graph[node]):
            if visited[nextnode] == 0:
                stack.append(nextnode)


for _ in visited[1:]:
    print(_)


