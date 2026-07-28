// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

import java.util.Arrays;

class Solution {
    public int assignBikes(int[][] workers, int[][] bikes) {
        int[][] memo = new int[workers.length][1 << bikes.length];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        return dp(0, 0, workers, bikes, memo);
    }

    private int dp(int i, int mask, int[][] workers, int[][] bikes, int[][] memo) {
        if (i == workers.length) {
            return 0;
        }
        if (memo[i][mask] != -1) {
            return memo[i][mask];
        }
        int best = Integer.MAX_VALUE;
        int wx = workers[i][0], wy = workers[i][1];
        for (int b = 0; b < bikes.length; b++) {
            if ((mask & (1 << b)) != 0) {
                continue;
            }
            int dist = Math.abs(wx - bikes[b][0]) + Math.abs(wy - bikes[b][1]);
            best = Math.min(best, dist + dp(i + 1, mask | (1 << b), workers, bikes, memo));
        }
        memo[i][mask] = best;
        return best;
    }
}
