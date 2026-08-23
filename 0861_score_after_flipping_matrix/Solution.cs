// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

using System;

public class Solution {
    public int MatrixScore(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        foreach (var row in grid) {
            if (row[0] == 0)
                for (int j = 0; j < n; j++) row[j] ^= 1;
        }
        int ans = m * (1 << (n - 1));
        for (int j = 1; j < n; j++) {
            int ones = 0;
            for (int i = 0; i < m; i++) ones += grid[i][j];
            ans += Math.Max(ones, m - ones) * (1 << (n - 1 - j));
        }
        return ans;
    }
}
