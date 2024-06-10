def solution(players, callings):
    dict = {}
    N = len(players)
    for i in range(N):
        dict[players[i]] = i
    
    for call in callings:
        inx = dict[call]
        if inx == 0:
            continue
        target = players[inx-1]
        players[inx], players[inx - 1] = target, call
        dict[call] = inx - 1
        dict[target] = inx
            
    answer = players
    return answer