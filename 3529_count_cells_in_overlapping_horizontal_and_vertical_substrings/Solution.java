// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

class Solution {
    public int countCells(char[][] grid, String pattern) {
        int m = grid.length, n = grid[0].length;
        var row = new StringBuilder(m * n);
        var col = new StringBuilder(m * n);
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) row.append(grid[i][j]);
        for (int j = 0; j < n; j++) for (int i = 0; i < m; i++) col.append(grid[i][j]);
        String rowS = row.toString(), colS = col.toString();
        boolean[][] hMark = new boolean[m][];
        boolean[][] vMark = new boolean[m][];
        for (int i = 0; i < m; i++) { hMark[i] = new boolean[n]; vMark[i] = new boolean[n]; }
        int plen = pattern.length();
        for (int i = 0; i + plen <= rowS.length(); i++) {
            if (rowS.substring(i, plen) == pattern) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    hMark[pos / n][pos % n] = true;
                }
            }
        }
        for (int i = 0; i + plen <= colS.length(); i++) {
            if (colS.substring(i, plen) == pattern) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    vMark[pos % m][pos / m] = true;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++)
            if (hMark[i][j] && vMark[i][j]) ans++;
        return ans;
    }
}
