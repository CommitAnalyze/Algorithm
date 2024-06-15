def binary(n, times, start, end):
    while start < end:
        mid = ( start + end ) // 2
        count = 0
        for time in times:
            count += mid // time
            if count > n:
                break
        if count >= n:
            end = mid
        else:
            start = mid + 1
    return end

def solution(n, times):
    N = len(times)
    times.sort()
    maxTime = n * times[-1] // N
    
    answer = binary(n, times, 0, maxTime)
    return answer
