// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

public class Solution {
    public int ButtonWithLongestTime(int[][] events) {
        int bestT = events[0][1], bestI = events[0][0];
        for (int i = 1; i < events.Length; i++) {
            int t = events[i][1] - events[i - 1][1];
            if (t > bestT || (t == bestT && events[i][0] < bestI)) {
                bestT = t;
                bestI = events[i][0];
            }
        }
        return bestI;
    }
}
