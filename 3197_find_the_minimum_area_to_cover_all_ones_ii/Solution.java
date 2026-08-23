// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

class Solution {
    public int minimumSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int ans = m * n;
        for (int i1 = 0; i1 < m - 1; i1++) {
            for (int i2 = i1 + 1; i2 < m - 1; i2++) {
                ans = Math.min(ans, area(grid, 0, 0, i1, n - 1) + area(grid, i1 + 1, 0, i2, n - 1) + area(grid, i2 + 1, 0, m - 1, n - 1));
            }
        }
        for (int j1 = 0; j1 < n - 1; j1++) {
            for (int j2 = j1 + 1; j2 < n - 1; j2++) {
                ans = Math.min(ans, area(grid, 0, 0, m - 1, j1) + area(grid, 0, j1 + 1, m - 1, j2) + area(grid, 0, j2 + 1, m - 1, n - 1));
            }
        }
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                ans = Math.min(ans, area(grid, 0, 0, i, j) + area(grid, 0, j + 1, i, n - 1) + area(grid, i + 1, 0, m - 1, n - 1));
                ans = Math.min(ans, area(grid, 0, 0, i, n - 1) + area(grid, i + 1, 0, m - 1, j) + area(grid, i + 1, j + 1, m - 1, n - 1));
                ans = Math.min(ans, area(grid, 0, 0, i, j) + area(grid, i + 1, 0, m - 1, j) + area(grid, 0, j + 1, m - 1, n - 1));
                ans = Math.min(ans, area(grid, 0, 0, m - 1, j) + area(grid, 0, j + 1, i, n - 1) + area(grid, i + 1, j + 1, m - 1, n - 1));
            }
        }
        return ans;
    }

    private int area(int[][] grid, int i1, int j1, int i2, int j2) {
        final int inf = Integer.MAX_VALUE / 4;
        int x1 = inf, y1 = inf, x2 = -inf, y2 = -inf;
        for (int i = i1; i <= i2; i++) {
            for (int j = j1; j <= j2; j++) {
                if (grid[i][j] == 1) {
                    x1 = Math.min(x1, i);
                    y1 = Math.min(y1, j);
                    x2 = Math.max(x2, i);
                    y2 = Math.max(y2, j);
                }
            }
        }
        if (x1 == inf) {
            return 0;
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1);
    }
}
