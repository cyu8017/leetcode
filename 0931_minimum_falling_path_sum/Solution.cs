// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

using System;
using System.Linq;

public class Solution {
    public int MinFallingPathSum(int[][] matrix) {
        int[] dp = (int[])matrix[0].Clone();
        for (int r = 1; r < matrix.Length; r++) {
            int[] ndp = new int[dp.Length];
            for (int c = 0; c < dp.Length; c++) {
                int best = dp[c];
                if (c > 0) best = Math.Min(best, dp[c - 1]);
                if (c + 1 < dp.Length) best = Math.Min(best, dp[c + 1]);
                ndp[c] = matrix[r][c] + best;
            }
            dp = ndp;
        }
        return dp.Min();
    }
}
