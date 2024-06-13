
dict = {}
count = []
def unifind(x):
    global dict
    X = dict[x]
    if X == x:
        return x
    dict[x] = unifind(X)
    return dict[x]


def uniset(a, b):
    global count
    global dict
    A = unifind(a)
    B = unifind(b)

    if A == B:
        return
    else:
        dict[B] = dict[A]
        count[A] += count[B]

def solution(n, wires):
    minValue = 999999999
    for j in range(n - 1):
        for i in range(1, n + 1):
            dict[i] = i

        count.clear()
        count.extend(list(1 for _ in range(n + 1)))
        for k in range(n - 1):
            if j == k:
                continue
            a, b = wires[k]
            uniset(a, b)
        numSet = set()
        for i in range(1, n + 1):
            numSet.add(unifind(i))
        numSet = sorted(numSet)
        midMin = abs(count[numSet[0]] - count[numSet[1]])
        if midMin < minValue:
            minValue = midMin
    answer = minValue
    return answer