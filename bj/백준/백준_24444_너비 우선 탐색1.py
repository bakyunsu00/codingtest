from collections import deque
import sys

#Bfs

input = sys.stdin.readline
N,M,R = map(int,(input().split(" ")))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,(input().split(" ")))
    graph[u].append(v)
    graph[v].append(u)






queue = deque()
visited = [0] * (N+1)
queue.append(R)
order = 1
while queue:
    node = queue.popleft()
    if not visited[node]:
        visited[node] = order
        order += 1
        for nxt in sorted( graph[node]):
            if not visited[nxt]:
                queue.append(nxt)


for _ in visited[1:]:
    print(_)
    #풀었다~