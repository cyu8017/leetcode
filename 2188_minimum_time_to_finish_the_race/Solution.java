// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

import java.util.Arrays;

class Solution {
    public int minimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        int[] minTime = new int[20];
        Arrays.fill(minTime, 1 << 30);
        for (int[] tire : tires) {
            int f = tire[0], r = tire[1];
            long t = f, lap = f;
            for (int x = 1; x < 20 && t < minTime[x]; x++) {
                minTime[x] = (int) t;
                lap *= r;
                if (lap > changeTime + f) break;
                t += lap;
            }
        }
        int[] dp = new int[numLaps + 1];
        Arrays.fill(dp, 1 << 30);
        dp[0] = -changeTime;
        for (int i = 1; i <= numLaps; i++)
            for (int j = 1; j <= i && j < 20; j++)
                dp[i] = Math.min(dp[i], dp[i - j] + changeTime + minTime[j]);
        return dp[numLaps];
    }
}
