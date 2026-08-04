// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

class Solution {
    public int getMaximumGold(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int ans = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != 0) ans = Math.max(ans, dfs(grid, r, c));
            }
        }
        return ans;
    }

    private int dfs(int[][] grid, int r, int c) {
        int gold = grid[r][c];
        grid[r][c] = 0;
        int best = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];
            if (nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[0].length && grid[nr][nc] != 0) {
                best = Math.max(best, dfs(grid, nr, nc));
            }
        }
        grid[r][c] = gold;
        return gold + best;
    }
}
