// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

public class Solution {
    public int MaximalSquare(char[][] matrix) {
        if (matrix == null || matrix.Length == 0) {
            return 0;
        }
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int[] dp = new int[cols + 1];
        int maxSide = 0;
        int prev = 0;
        for (int row = 1; row <= rows; row++) {
            for (int col = 1; col <= cols; col++) {
                int temp = dp[col];
                if (matrix[row - 1][col - 1] == '1') {
                    dp[col] = Math.Min(dp[col], Math.Min(dp[col - 1], prev)) + 1;
                    maxSide = Math.Max(maxSide, dp[col]);
                } else {
                    dp[col] = 0;
                }
                prev = temp;
            }
        }
        return maxSide * maxSide;
    }
}
