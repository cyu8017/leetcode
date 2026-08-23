// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

public class Solution {
    public bool ContainsCycle(char[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        bool[,] seen = new bool[m, n];
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };

        bool Dfs(int r, int c, int pr, int pc) {
            seen[r, c] = true;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] != grid[r][c] || (nr == pr && nc == pc))
                    continue;
                if (seen[nr, nc] || Dfs(nr, nc, r, c)) return true;
            }
            return false;
        }

        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if (!seen[r, c] && Dfs(r, c, -1, -1)) return true;
        return false;
    }
}
