// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution {
    public int countSubmatrices(int[][] grid, int k) {
        int n = grid.length, m = grid[0].length, ans = 0;
        int[][] s = new int[n + 1][];
        for (int i = 0; i <= n; i++) s[i] = new int[m + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j];
                if (s[i + 1][j + 1] <= k) ans++;
            }
        }
        return ans;
    }
}
