import java.util.Arrays;

class Solution {
    int low, high, mid, cnt;

    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        Arrays.sort(rocks);
        low = 1;
        high = distance;

        while(low <= high){
            mid = low + (high - low) / 2;
            cnt = 0;
            // remove rocks;
            cnt = removeRocks(rocks, distance);

            if(cnt <= n){
                low = mid + 1;
                answer = mid;
            }
            else{
                high = mid - 1;
            }
        }
        return answer;
    }

    int removeRocks(int[] rocks, int distance){
        int start = 0;
        for(int i = 0; i<rocks.length; i++){
            if(rocks[i] - start < mid) {
                cnt++;
            }
            else {
                start = rocks[i];
            }
        }

        // 끝까지 돌을 다 제거해도 mid보다 작으면 거리가 mid보다 작은게 존재한다는 뜻임
        if(distance - start < mid) {
            return ++cnt;
        }

        return cnt;
    }
}
