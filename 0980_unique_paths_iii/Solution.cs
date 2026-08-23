// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

public class Solution {
    public int UniquePathsIII(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int empty = 0, sr = 0, sc = 0, ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != -1) empty++;
                if (grid[i][j] == 1) { sr = i; sc = j; }
            }
        }
        void Dfs(int r, int c, int remain) {
            if (grid[r][c] == 2) {
                if (remain == 1) ans++;
                return;
            }
            int temp = grid[r][c];
            grid[r][c] = -1;
            int[][] dirs = new int[][] { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1)
                    Dfs(nr, nc, remain - 1);
            }
            grid[r][c] = temp;
        }
        Dfs(sr, sc, empty);
        return ans;
    }
}
