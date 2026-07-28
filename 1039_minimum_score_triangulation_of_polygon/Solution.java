// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

import java.util.Arrays;

class Solution {
    public int minScoreTriangulation(int[] values) {
        int n = values.length;
        int[][] memo = new int[n][n];
        for (int[] row : memo) Arrays.fill(row, -1);
        return dp(values, 0, n - 1, memo);
    }

    private int dp(int[] values, int i, int j, int[][] memo) {
        if (j - i < 2) return 0;
        if (memo[i][j] != -1) return memo[i][j];
        int best = Integer.MAX_VALUE;
        for (int k = i + 1; k < j; k++) {
            best = Math.min(best, dp(values, i, k, memo) + values[i] * values[k] * values[j] + dp(values, k, j, memo));
        }
        return memo[i][j] = best;
    }
}
