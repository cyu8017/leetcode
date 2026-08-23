// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution {
    private int[][] grid;
    private int m, n;
    private final int[] dirs = {-1, 0, 1, 0, -1};

    private long dfs(int i, int j) {
        long s = grid[i][j];
        grid[i][j] = 0;
        for (int d = 0; d < 4; d++) {
            int x = i + dirs[d], y = j + dirs[d + 1];
            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0) s += dfs(x, y);
        }
        return s;
    }

    public int countIslands(int[][] grid, int k) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0 && dfs(i, j) % k == 0) ans++;
        return ans;
    }
}
