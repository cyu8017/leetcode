// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

import java.util.Arrays;

class Solution {
    private static final int[][] DIRS = {
        {1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
    };

    public int[][] tourOfKnight(int m, int n, int r, int c) {
        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++) Arrays.fill(ans[i], -1);
        dfs(ans, m, n, r, c, 0);
        return ans;
    }

    private boolean dfs(int[][] ans, int m, int n, int x, int y, int step) {
        ans[x][y] = step;
        if (step == m * n - 1) return true;
        for (int[] d : DIRS) {
            int nx = x + d[0], ny = y + d[1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1)
                if (dfs(ans, m, n, nx, ny, step + 1)) return true;
        }
        ans[x][y] = -1;
        return false;
    }
}
