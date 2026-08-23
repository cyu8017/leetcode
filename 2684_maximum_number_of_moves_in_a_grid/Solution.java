// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
    public int maxMoves(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] dp = new int[m];
        for (int c = n - 2; c >= 0; c--) {
            int[] ndp = new int[m];
            for (int r = 0; r < m; r++) {
                int best = 0;
                for (int dr = -1; dr <= 1; dr++) {
                    int nr = r + dr;
                    if (nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c])
                        best = Math.max(best, 1 + dp[nr]);
                }
                ndp[r] = best;
            }
            dp = ndp;
        }
        int ans = 0;
        for (int v : dp) ans = Math.max(ans, v);
        return ans;
    }
}
