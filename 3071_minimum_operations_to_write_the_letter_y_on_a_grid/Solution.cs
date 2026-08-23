// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

using System;

public class Solution {
    public int MinimumOperationsToWriteY(int[][] grid) {
        int n = grid.Length;
        int[] cnt1 = new int[3], cnt2 = new int[3];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int x = grid[i][j];
                bool a = i == j && i <= n / 2;
                bool b = i + j == n - 1 && i <= n / 2;
                bool c = j == n / 2 && i >= n / 2;
                if (a || b || c) cnt1[x]++;
                else cnt2[x]++;
            }
        }
        int ans = n * n;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (i != j) ans = Math.Min(ans, n * n - cnt1[i] - cnt2[j]);
        return ans;
    }
}
