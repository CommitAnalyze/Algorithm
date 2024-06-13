import java.util.*;

class Solution {
    
    Map<String, Integer> map = new HashMap<>();
    Map<Integer, String> ranks = new HashMap<>();
    
    public String[] solution(String[] players, String[] callings) {
        int len = players.length;
        String[] answer = new String[len];
        
        for(int i = 0; i< len; i++){
            map.put(players[i], i+1);
            ranks.put(i+1, players[i]);
        }
        
        
        for(String c : callings){
            int tempRank = map.get(c);
            String pre = ranks.get(tempRank-1);
            map.put(c, tempRank - 1);
            map.put(pre, tempRank);
            ranks.put(tempRank-1, c);
            ranks.put(tempRank, pre);
            
        }
        for(int i = 0; i < len; i++){
            answer[i] = ranks.get(i+1);
        }
        return answer;
    }
}
