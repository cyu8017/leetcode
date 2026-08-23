// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        final int MOD = 1000000007;
        int[][] dp = new int[m][n];
        dp[startRow][startColumn] = 1;
        int result = 0;
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int move = 0; move < maxMove; ++move) {
            int[][] nxt = new int[m][n];
            for (int row = 0; row < m; ++row) {
                for (int col = 0; col < n; ++col) {
                    int ways = dp[row][col];
                    if (ways == 0) {
                        continue;
                    }
                    for (int[] dir : dirs) {
                        int nr = row + dir[0];
                        int nc = col + dir[1];
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
