// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

using System.Text;

public class Solution {
    public int CountCells(char[][] grid, string pattern) {
        int m = grid.Length, n = grid[0].Length;
        var row = new StringBuilder(m * n);
        var col = new StringBuilder(m * n);
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) row.Append(grid[i][j]);
        for (int j = 0; j < n; j++) for (int i = 0; i < m; i++) col.Append(grid[i][j]);
        string rowS = row.ToString(), colS = col.ToString();
        bool[][] hMark = new bool[m][];
        bool[][] vMark = new bool[m][];
        for (int i = 0; i < m; i++) { hMark[i] = new bool[n]; vMark[i] = new bool[n]; }
        int plen = pattern.Length;
        for (int i = 0; i + plen <= rowS.Length; i++) {
            if (rowS.Substring(i, plen) == pattern) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    hMark[pos / n][pos % n] = true;
                }
            }
        }
        for (int i = 0; i + plen <= colS.Length; i++) {
            if (colS.Substring(i, plen) == pattern) {
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
