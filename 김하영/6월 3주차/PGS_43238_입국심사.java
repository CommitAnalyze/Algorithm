import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long low = 1;
        long high = (long)times[times.length-1] * n;
        long mid = 0;
        long cnt = 0;
        long answer = 0;
        
        while(high >= low){
            mid = low + (high - low) / 2;
            cnt = 0;
            for(int time : times) cnt += mid/time;
            
            if(cnt >= n){ // 시간 안에 n명의 사람들을 다 심사할 수 있다면 범위 좁히기
                answer = mid;
                high = mid - 1;
            } else{ // 시간 안에 n명의 사람들을 심사 할 수 없다면 범위 늘리기
                low = mid + 1;
            }
        }
        
        return answer;
    }
}
