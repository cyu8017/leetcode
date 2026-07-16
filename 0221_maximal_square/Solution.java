// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            return 0;
        }
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[] dp = new int[cols + 1];
        int maxSide = 0;
        int prev = 0;
        for (int row = 1; row <= rows; row++) {
            for (int col = 1; col <= cols; col++) {
                int temp = dp[col];
                if (matrix[row - 1][col - 1] == '1') {
                    dp[col] = Math.min(dp[col], Math.min(dp[col - 1], prev)) + 1;
                    maxSide = Math.max(maxSide, dp[col]);
                } else {
                    dp[col] = 0;
                }
                prev = temp;
            }
        }
        return maxSide * maxSide;
    }
}
