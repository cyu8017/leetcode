// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

public class Solution {
    public int FindPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        const int MOD = 1000000007;
        int[][] dp = new int[m][];
        for (int i = 0; i < m; ++i) dp[i] = new int[n];
        dp[startRow][startColumn] = 1;
        int result = 0;
        int[][] dirs = new int[][] { new[]{0,1}, new[]{0,-1}, new[]{1,0}, new[]{-1,0} };

        for (int move = 0; move < maxMove; ++move) {
            int[][] nxt = new int[m][];
            for (int i = 0; i < m; ++i) nxt[i] = new int[n];
            for (int row = 0; row < m; ++row) {
                for (int col = 0; col < n; ++col) {
                    int ways = dp[row][col];
                    if (ways == 0) continue;
                    foreach (var d in dirs) {
                        int nr = row + d[0], nc = col + d[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                            nxt[nr][nc] = (nxt[nr][nc] + ways) % MOD;
                        } else {
                            result = (result + ways) % MOD;
                        }
                    }
                }
            }
            dp = nxt;
        }
        return result;
    }
}
