// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

import java.util.*;

class Solution {
    public int[][] differenceOfDistinctValues(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Set<Integer> top = new HashSet<>();
                Set<Integer> bot = new HashSet<>();
                for (int r = i - 1, c = j - 1; r >= 0 && c >= 0; r--, c--) top.add(grid[r][c]);
                for (int r = i + 1, c = j + 1; r < m && c < n; r++, c++) bot.add(grid[r][c]);
                ans[i][j] = Math.abs(top.size() - bot.size());
            }
        }
        return ans;
    }
}
