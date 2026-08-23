// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution {
    public boolean satisfiesConditions(int[][] grid) {
        int m = grid.length, n = grid[0].length;
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
