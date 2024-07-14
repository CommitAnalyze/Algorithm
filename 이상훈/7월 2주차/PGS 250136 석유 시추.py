from collections import deque

dij = [(1,0),(0,1),(-1,0),(0,-1)]
def BFS(i, j, land, cntList, n, m):
    q = deque()
    q.append((i,j))
    land[i][j] = 0
    cnt = 1
    mSet = set([j])
    while q:
        a, b = q.popleft()
        for dx, dy in dij:
            x = a + dx
            y = b + dy
            if 0<=x<n and 0<=y<m and land[x][y] == 1:
                cnt += 1
                mSet.add(y)
                land[x][y] = 0
                q.append((x,y))
    for m in mSet:
        cntList[m] += cnt
    return

def solution(land):
    n = len(land)
    m = len(land[0])
    cntList = list(0 for _ in range(m))
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                BFS(i, j, land, cntList, n, m)
    answer = max(cntList)
    return answer
