from collections import deque

dij = [(0,1),(1,0),(0,-1),(-1,0)]

def BFS(i, j, N, M, newMaps):
    q = deque()
    q.append((i,j))
    cnt = int(newMaps[i][j])
    newMaps[i][j] = 'X'
    while q:
        now = q.popleft()
        for x, y in dij:
            dx = now[0] + x
            dy = now[1] + y
            if 0<=dx<N and 0<=dy<M and newMaps[dx][dy] != 'X':
                q.append((dx,dy))
                cnt += int(newMaps[dx][dy])
                newMaps[dx][dy] = 'X'
    return cnt
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    newMaps = list(list('' for _ in range(M)) for __ in range(N))

    # 방문자 체크용 맵을 따로 쓰지 않기 위해 문자열을 리스트로 변형하여 진행
    for i in range(N):
        for j in range(M):
            newMaps[i][j] = maps[i][j]
    answer = []
    
    for i in range(N):
        for j in range(M):
            if newMaps[i][j] != 'X':
                food = BFS(i, j, N, M, newMaps)
                answer.append(food)
    
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer
