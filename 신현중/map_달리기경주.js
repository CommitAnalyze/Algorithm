function solution(players, callings) {
  //obj 로 조회 빠르게
  const playerMap = {};
  for (
    let i = 0;
    i < players.length;
    i++
  ) {
    playerMap[players[i]] = i;
  }

  for (
    let i = 0;
    i < callings.length;
    i++
  ) {
    const cp = callings[i];
    const idx = playerMap[cp];
    const temp = players[idx - 1];

    //players의 인덱스의 값 변경
    players[idx - 1] = cp;
    players[idx] = temp;

    // obj의 idx도 갱신
    playerMap[cp] = idx - 1;
    playerMap[temp] = idx;
  }

  return players;
}
