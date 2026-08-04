// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution {
    public int minFallingPathSum(int[][] grid) {
        int[] dp = grid[0].clone();
        for (int rowIndex = 1; rowIndex < grid.length; rowIndex++) {
            int[] row = grid[rowIndex];
            int first = 0;
            for (int i = 1; i < dp.length; i++) {
                if (dp[i] < dp[first]) first = i;
            }
            int secondValue = Integer.MAX_VALUE;
            for (int i = 0; i < dp.length; i++) {
                if (i != first) secondValue = Math.min(secondValue, dp[i]);
            }
            if (dp.length == 1) secondValue = 0;
            int[] next = new int[dp.length];
            for (int i = 0; i < row.length; i++) {
                next[i] = row[i] + (i == first ? secondValue : dp[first]);
            }
            dp = next;
        }
        int best = dp[0];
        for (int value : dp) best = Math.min(best, value);
        return best;
    }
}
