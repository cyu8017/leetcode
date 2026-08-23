// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

public class Solution {
    public bool PossibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        int m = grid.Length, n = grid[0].Length;
        int[][] pref = new int[m + 1][];
        for (int i = 0; i <= m; i++) pref[i] = new int[n + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j];
        int Sum(int r1, int c1, int r2, int c2) {
            return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1];
        }
        int[][] diff = new int[m + 1][];
        for (int i = 0; i <= m; i++) diff[i] = new int[n + 1];
        for (int i = 0; i + stampHeight - 1 < m; i++) {
            for (int j = 0; j + stampWidth - 1 < n; j++) {
                if (Sum(i, j, i + stampHeight - 1, j + stampWidth - 1) == 0) {
                    diff[i][j]++;
                    diff[i][j + stampWidth]--;
                    diff[i + stampHeight][j]--;
                    diff[i + stampHeight][j + stampWidth]++;
                }
            }
        }
        int[][] cur = new int[m][];
        for (int i = 0; i < m; i++) cur[i] = new int[n];
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
