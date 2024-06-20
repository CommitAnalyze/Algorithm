const bfs = (start, exNode, G) => {
  let q = [start];
  let visited = {};
  for (v of Object.keys(G)) {
    visited[v] = false;
  }
  visited[start] = true;
  visited[exNode] = true;
  //console.log(visited)
  //console.log('start',start, exNode)
  let cnt = 1;
  while (q.length !== 0) {
    v = q.pop();
    //if(visited[v]===true){continue}
    visited[v] = true;
    for (nv of G[v]) {
      if (visited[nv] === true) {
        //console.log('asdasd',nv)
        continue;
      }
      q.push(nv);
      visited[nv] = true;
    }
    //console.log(v,q, cnt)
    cnt++;
  }
  //console.log(start, exNode,cnt)
  return cnt;
};

function solution(n, wires) {
  var answer = n;

  const G = {};
  for ([w0, w1] of wires) {
    //console.log(w)
    if (w0 in G) {
      G[w0].push(w1);
    } else {
      G[w0] = [w1];
    }
    if (w1 in G) {
      G[w1].push(w0);
    } else {
      G[w1] = [w0];
    }
  }
  //console.log(G)

  for ([w0, w1] of wires) {
    answer = Math.min(
      answer,
      Math.abs(
        bfs(w0, w1, G) - bfs(w1, w0, G)
      )
    );
  }

  return answer;
}
