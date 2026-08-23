// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

public class Solution {
    public int CountPaths(int[][] grid) {
        const int mod = 1000000007;
        int m = grid.Length, n = grid[0].Length;
        var dp = new int[m][];
        for (int i = 0; i < m; i++) dp[i] = new int[n];
        int[][] dirs = new int[][] { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
        int Dfs(int r, int c) {
            if (dp[r][c] != 0) return dp[r][c];
            int res = 1;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c])
                    res = (res + Dfs(nr, nc)) % mod;
            }
            return dp[r][c] = res;
        }
        int ans = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                ans = (ans + Dfs(i, j)) % mod;
        return ans;
    }
}
