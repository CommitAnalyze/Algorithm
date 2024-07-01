from collections import deque
result = 99999999

def solution(x, y, n):
    global result
    
    if x + n == y:
        return 1
    
    # BT(x, 0, y, n)
    q = deque()
    q.append((y, 0))
    while q:
        A, cnt = q.popleft()
        if A == x:
            result = cnt
            break
        if A % 3 == 0 and A//3 >= x:
            q.append((A//3, cnt+1))
        if A % 2 == 0 and A//2 >= x:
            q.append((A//2, cnt+1))
        if A - n >= x:
            q.append((A-n, cnt+1))
    answer = result
    if answer == 99999999:
        return -1
    return answer
