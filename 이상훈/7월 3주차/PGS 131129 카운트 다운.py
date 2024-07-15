"""
1 ~ 20 / *2 *3
22 24 26 28 ~~~ 40
21 24 27 30 33 36 39 42 45 48 51 54 57 60 
50

150 => 50 3 / 60 60 30 

"""
dtSet = set()
greatList = list(range(1, 21))
greatList.append(50)
for i in range(1, 21):
    if i*2 > 20:
        dtSet.add(i*2)
    if i*3 > 20:
        dtSet.add(i*3)

result  = list([999999999, 999999999] for _ in range(100061))
result[0] = [0, 0]
for i in range(0, 100000):
    for num in greatList:
        if result[num+i][0] > result[i][0] + 1:
            result[num+i] = [result[i][0]+1, result[i][1]+1]
        elif result[num+i][0] == result[i][0]+1 and result[num+i][1] < result[i][1] + 1:
            result[num+i][1] = result[i][1] + 1
    for mul in dtSet:
        if result[mul+i][0] > result[i][0] + 1:
            result[mul+i] = [result[i][0]+1, result[i][1]]
        elif result[mul+i][0] == result[i][0]+1 and result[mul+i][1] < result[i][1]:
            result[mul+i][1] = result[i][1]
    
def solution(target):
    global result
    answer = result[target]
    return answer
