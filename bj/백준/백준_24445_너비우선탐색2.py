import sys
from collections import deque
input = sys.stdin.readline

N, M, R = list(map(int,(input().split(" "))))

graph = [[] for _ in range(0,N+1)]
queue = deque()
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u,v = list(map(int,(input().split())))
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse = True)

def bfs(graph,visited,R):
    count = 1
    queue.append(R)
    visited[R] = count

    while queue:
        num = queue.popleft()
        for node in graph[num]:
            if visited[node] == 0:
                count += 1
                visited[node] = count
                queue.append(node)


    return visited



result = bfs(graph,visited,R)
for _ in result[1:]:
    print(_)








