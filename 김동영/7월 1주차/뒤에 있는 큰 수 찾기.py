from collections import deque

def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = deque([])
    for i in range(N) :
        value = numbers[i]
        while stack and numbers[stack[-1]] < value:
            answer[stack[-1]] = value
            stack.pop()
        stack.append(i)

    return answer
