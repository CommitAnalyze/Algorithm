function solution(distance, rocks, n) {
  var answer = 0;
  // 정렬 및 시작점과 끝점 추가
  rocks = [
    0,
    ...rocks.sort((a, b) => a - b),
    distance,
  ];
  let min = 0;
  let max = distance;
  // 이진탐색
  while (min <= max) {
    let mid = Math.floor(
      (max + min) / 2
    );

    let removeRocks = 0;
    let prevRock = 0;
    for (
      let i = 1;
      i < rocks.length;
      i++
    ) {
      // mid는 최소 거리, mid보다 작은 거리의 바위는 제거
      if (rocks[i] - prevRock < mid) {
        removeRocks++;
      } else {
        prevRock = rocks[i];
      }
    }
    // 최소 거리가 커서 제거한 바위가 n보다 많으면
    //최소 거리를 줄인다.
    if (removeRocks > n) {
      max = mid - 1;
    } else {
      // 최소 거리가 작으면 최소 거리를 늘린다.
      min = mid + 1;
    }
    answer = max;
  }
  return answer;
}
