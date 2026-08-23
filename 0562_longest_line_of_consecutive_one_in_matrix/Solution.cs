// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

public class Solution {
    public int LongestLine(int[][] mat) {
        if (mat == null || mat.Length == 0 || mat[0].Length == 0) return 0;
        int rows = mat.Length, cols = mat[0].Length;
        int[,,] dp = new int[rows, cols, 4];
        int best = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (mat[r][c] == 0) continue;
                dp[r, c, 0] = (c > 0 ? dp[r, c - 1, 0] : 0) + 1;
                dp[r, c, 1] = (r > 0 ? dp[r - 1, c, 1] : 0) + 1;
                dp[r, c, 2] = (r > 0 && c > 0 ? dp[r - 1, c - 1, 2] : 0) + 1;
                dp[r, c, 3] = (r > 0 && c + 1 < cols ? dp[r - 1, c + 1, 3] : 0) + 1;
                for (int k = 0; k < 4; ++k) if (dp[r, c, k] > best) best = dp[r, c, k];
            }
        }
        return best;
    }
}
