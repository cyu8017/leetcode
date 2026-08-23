// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

class Solution {
    private int ans;
    private int m, n;
    private int[][] grid;

    public int uniquePathsIII(int[][] grid) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        int empty = 0, sr = 0, sc = 0;
        ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != -1) empty++;
                if (grid[i][j] == 1) { sr = i; sc = j; }
            }
        }
        dfs(sr, sc, empty);
        return ans;
    }

    private void dfs(int r, int c, int remain) {
        if (grid[r][c] == 2) {
            if (remain == 1) ans++;
            return;
        }
        int temp = grid[r][c];
        grid[r][c] = -1;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1)
                dfs(nr, nc, remain - 1);
        }
        grid[r][c] = temp;
    }
}
