// LeetCode 1267 - Count Servers That Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

public class Solution {
    public int CountServers(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var rows = new int[m];
        var cols = new int[n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    rows[r]++;
                    cols[c]++;
                }
            }
        }
        int count = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1 && (rows[r] > 1 || cols[c] > 1)) count++;
            }
        }
        return count;
    }
}
