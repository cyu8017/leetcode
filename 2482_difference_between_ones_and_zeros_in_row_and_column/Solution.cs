// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

public class Solution {
    public int[][] OnesMinusZeros(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[] row = new int[m], col = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row[i] += grid[i][j];
                col[j] += grid[i][j];
            }
        }
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) {
            ans[i] = new int[n];
            for (int j = 0; j < n; j++)
                ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j]);
        }
        return ans;
    }
}
