// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution {
    public boolean containsCycle(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] seen = new boolean[m][n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (!seen[r][c] && dfs(grid, seen, r, c, -1, -1)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] grid, boolean[][] seen, int r, int c, int pr, int pc) {
        seen[r][c] = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) {
                continue;
            }
            if (grid[nr][nc] != grid[r][c] || (nr == pr && nc == pc)) {
                continue;
            }
            if (seen[nr][nc] || dfs(grid, seen, nr, nc, r, c)) {
                return true;
            }
        }
        return false;
    }
}
