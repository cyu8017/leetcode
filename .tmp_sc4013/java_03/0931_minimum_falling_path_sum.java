// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int[] dp = matrix[0].clone();
        for (int r = 1; r < matrix.length; r++) {
            int[] ndp = new int[dp.length];
            for (int c = 0; c < dp.length; c++) {
                int best = dp[c];
                if (c > 0) best = Math.min(best, dp[c - 1]);
                if (c + 1 < dp.length) best = Math.min(best, dp[c + 1]);
                ndp[c] = matrix[r][c] + best;
            }
            dp = ndp;
        }
        int ans = dp[0];
        for (int x : dp) ans = Math.min(ans, x);
        return ans;
    }
}
