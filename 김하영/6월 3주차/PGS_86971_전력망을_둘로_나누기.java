import java.util.*;

class Solution {
    
    int[][] adjList;
    boolean[] visit;
    
    public int solution(int n, int[][] wires) {
        int answer = n;
        
        for(int i = 0; i<wires.length; i++){
            // 인접 리스트 생성
            adjList = new int[n+1][n+1];
            for(int j = 0; j<wires.length; j++){
                if(j == i) continue;
                int start = wires[j][0];
                int end = wires[j][1];
                adjList[start][end] = 1;
                adjList[end][start] = 1;
            }
            
            // 1번 노드에서부터 개수 새기
            int count = BFS(n);
            
            // answer min으로 업데이트
            answer = Math.min(answer, Math.abs(n - count - count)); 
        }
        
        return answer;
    }
    
    public int BFS(int n){
        int count = 0;
        visit = new boolean[n+1];
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(1);
        count++;
        visit[1] = true;
        while(!q.isEmpty()){
            int cur = q.poll();
            for(int i = 1; i<n+1; i++){
                if(adjList[cur][i] != 0 && !visit[i]){
                    q.add(i);
                    visit[i] = true;
                    count++;
                }
            }
        }
        return count;
    }
}
