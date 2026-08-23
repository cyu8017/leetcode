// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

public class Solution {
    public bool SatisfiesConditions(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x = grid[i][j];
                if (i + 1 < m && x != grid[i + 1][j]) return false;
                if (j + 1 < n && x == grid[i][j + 1]) return false;
            }
        }
        return true;
    }
}
