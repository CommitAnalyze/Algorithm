"""
1
2 X A = 4 X B
본인이 2 일 때 기준 상대 무게 : 2/4 2/3
본인이 3 일 때 : 3/2 3/4
본인이 4 일 때 : 4/2 4/3
"""
multiple = [2/4, 2/3, 3/2, 3/4, 4/2, 4/3]
def solution(weights):
    cntList = list(0 for _ in range(1001))
    
    for i in range(len(weights)):
        cntList[weights[i]] += 1
        
    result = 0
    for w in weights:
        count = 0
        if cntList[w] > 1:
            count += (cntList[w]-1)
        for mul in multiple:
            num = w*mul
            if num == int(num) and 100<= num <=1000 and cntList[int(num)] > 0:
                count += cntList[int(num)]
        result += count
    answer = result//2
    return answer
