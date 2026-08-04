// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[][] memo;
    private int[] locations;
    private int finish;

    public int countRoutes(int[] locations, int start, int finish, int fuel) {
        this.locations = locations;
        this.finish = finish;
        memo = new int[locations.length][fuel + 1];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        return dp(start, fuel);
    }

    private int dp(int city, int left) {
        if (memo[city][left] != -1) {
            return memo[city][left];
        }
        long total = city == finish ? 1 : 0;
        for (int nxt = 0; nxt < locations.length; nxt++) {
            int cost = Math.abs(locations[city] - locations[nxt]);
            if (nxt != city && cost <= left) {
                total += dp(nxt, left - cost);
            }
        }
        memo[city][left] = (int) (total % MOD);
        return memo[city][left];
    }
}
