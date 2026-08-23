// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

class Solution {
    public boolean predictTheWinner(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = nums[i];
        }
        for (int length = 2; length <= n; length++) {
            for (int left = 0; left <= n - length; left++) {
                int right = left + length - 1;
                dp[left][right] = Math.max(
                        nums[left] - dp[left + 1][right],
                        nums[right] - dp[left][right - 1]
                );
            }
        }
        return dp[0][n - 1] >= 0;
    }
}
