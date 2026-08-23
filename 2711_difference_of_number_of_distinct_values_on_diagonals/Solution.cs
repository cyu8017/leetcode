// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] DifferenceOfDistinctValues(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                var top = new HashSet<int>();
                var bot = new HashSet<int>();
                for (int r = i - 1, c = j - 1; r >= 0 && c >= 0; r--, c--) top.Add(grid[r][c]);
                for (int r = i + 1, c = j + 1; r < m && c < n; r++, c++) bot.Add(grid[r][c]);
                ans[i][j] = Math.Abs(top.Count - bot.Count);
            }
        }
        return ans;
    }
}
