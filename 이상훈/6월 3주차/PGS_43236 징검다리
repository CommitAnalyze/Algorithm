def binary(distance, distList, n):
    start = 0
    end = distance
    while start <= end:
        mid = ( start + end ) // 2
        count = 0
        midDist = 0
        print(distList)
        for dist in distList:
            midDist += dist
            if midDist >= mid:
                midDist = 0
                continue
            else:
                count += 1
            if count > n:
                end = mid - 1
                break
        if count == n:
            start = mid + 1
        elif count < n:
            start = mid + 1
        # count 와 n 의 관계를 통해 start, end를 지정하는 부분이 진짜 헷갈림.
    return end
            
            
def solution(distance, rocks, n):
    rocks.sort()
    distList = [rocks[0]]
    for i in range(len(rocks)-1):
        distList.append(rocks[i+1]-rocks[i])
    distList.append(distance-rocks[-1])
    answer = binary(distance, distList[0:], n)

    return answer
