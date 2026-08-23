// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

public class Solution {
    public int MinimumOperations(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int ans = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 1; i < m; i++) {
                if (grid[i][j] <= grid[i - 1][j]) {
                    int need = grid[i - 1][j] + 1;
                    ans += need - grid[i][j];
                    grid[i][j] = need;
                }
            }
        }
        return ans;
    }
}
