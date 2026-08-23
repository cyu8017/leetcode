// LeetCode 2128 - Remove All Ones With Row and Column Flips
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

public class Solution {
    public bool RemoveOnes(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        for (int i = 1; i < m; i++) {
            bool same = grid[i][0] == grid[0][0];
            for (int j = 0; j < n; j++) {
                if ((grid[i][j] == grid[0][j]) != same) return false;
            }
        }
        return true;
    }
}
