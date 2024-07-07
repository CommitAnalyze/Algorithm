from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([destination])
    visited[destination] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)
    
    for i in sources:
        answer.append(visited[i])
    
    return answer
