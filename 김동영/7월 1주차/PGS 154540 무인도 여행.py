from collections import deque

def solution(maps):
    def bfs(x, y):
        q = deque()
        q.append([x, y])
        visited[x][y] = True
        days = 0
        while q:
            cx, cy = q.popleft()
            days += int(maps[cx][cy])
            for d in direct:
                nx, ny = cx + d[0], cy + d[1]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maps[nx][ny] != "X":
                    q.append([nx, ny])
                    visited[nx][ny] = True
        return days

    answer = []
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] != "X" and not visited[i][j]:
                answer.append(bfs(i, j))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
