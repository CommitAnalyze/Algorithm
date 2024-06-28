def solution(n, m, section):
    lineMAP = list(0 for _ in range(n))

    for num in section:
        lineMAP[num-1] = 1
    i = 0
    cnt = 0
    while i < n:
        if lineMAP[i] == 1:
            i += m
            cnt += 1
            continue
        i += 1
            
    answer = cnt
    
    return answer
