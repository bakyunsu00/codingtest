import sys
input = sys.stdin.readline

line = input().rstrip()

N,M,R = map(int,(line.split(" ")))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    input = sys.stdin.readline
    u,v = map(int,(input().split(" ")))
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

visited = [0] * (N+1)

stack = [R]
order = 1
while stack:
    node = stack.pop()
    if visited[node] == 0:
        visited[node] = order
        order += 1
        for i in sorted(graph[node],reverse=True):
            if visited[i] == 0:
                stack.append(i)

for _ in visited[1:]:
    print(_)





