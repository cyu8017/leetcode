// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

class Solution {
    public boolean possibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        int m = grid.length, n = grid[0].length;
        int[][] pref = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j];
        int[][] diff = new int[m + 1][n + 1];
        for (int i = 0; i + stampHeight - 1 < m; i++) {
            for (int j = 0; j + stampWidth - 1 < n; j++) {
                int sum = pref[i + stampHeight][j + stampWidth] - pref[i][j + stampWidth]
                        - pref[i + stampHeight][j] + pref[i][j];
                if (sum == 0) {
                    diff[i][j]++;
                    diff[i][j + stampWidth]--;
                    diff[i + stampHeight][j]--;
                    diff[i + stampHeight][j + stampWidth]++;
                }
            }
        }
        int[][] cur = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int v = diff[i][j];
                if (i > 0) v += cur[i - 1][j];
                if (j > 0) v += cur[i][j - 1];
                if (i > 0 && j > 0) v -= cur[i - 1][j - 1];
                cur[i][j] = v;
                if (grid[i][j] == 0 && v == 0) return false;
            }
        }
        return true;
    }
}
