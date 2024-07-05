from collections import deque
def BFS(destination, roadList, visited):
    q = deque()
    q.append((destination, 0))
    visited[destination] = 0
    while q:
        now, cnt = q.popleft()
        
        for road in roadList[now]:
            if visited[road] == -1:
                visited[road] = cnt+1
                q.append((road, cnt+1))
    return visited

def solution(n, roads, sources, destination):
    roadList = list([] for _ in range(n+1))
    visited = list(-1 for _ in range(len(roadList)))
    answer = []
    for road in roads:
        a, b = road
        roadList[a].append(b)
        roadList[b].append(a)

    result = BFS(destination, roadList, visited)
    for source in sources:
        answer.append(result[source])
        
    return answer
