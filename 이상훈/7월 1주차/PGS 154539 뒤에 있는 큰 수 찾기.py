from collections import deque
def solution(numbers):
    stack = []
    N = len(numbers)
    result = [0 for _ in range(N)]
    q = deque(numbers)

    i = 0
    while i < N:
        number = q.popleft()
        
        while stack and stack[-1][0] < number:
            num, ind = stack.pop()
            result[ind] = number
        
        stack.append((number,i))
        i += 1

    while stack:
        num, ind = stack.pop()
        result[ind] = -1
    answer = result
    
    return answer
