// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

class Solution {
    public int longestLine(int[][] mat) {
        if (mat.length == 0 || mat[0].length == 0) {
            return 0;
        }

        int rows = mat.length;
        int cols = mat[0].length;
        int[][][] dp = new int[rows][cols][4];
        int best = 0;

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (mat[r][c] == 0) {
                    continue;
                }
                dp[r][c][0] = (c > 0 ? dp[r][c - 1][0] : 0) + 1;
                dp[r][c][1] = (r > 0 ? dp[r - 1][c][1] : 0) + 1;
                dp[r][c][2] = (r > 0 && c > 0 ? dp[r - 1][c - 1][2] : 0) + 1;
                dp[r][c][3] = (r > 0 && c + 1 < cols ? dp[r - 1][c + 1][3] : 0) + 1;
                for (int d = 0; d < 4; ++d) {
                    best = Math.max(best, dp[r][c][d]);
                }
            }
        }
        return best;
    }
}
