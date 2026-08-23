// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

using System;

public class Solution {
    private int n;
    private int[][] grid;
    private int[,,] memo;

    public int CherryPickup(int[][] grid) {
        n = grid.Length;
        this.grid = grid;
        memo = new int[n, n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++)
                    memo[i, j, k] = int.MinValue;
        return Math.Max(0, Dp(0, 0, 0));
    }

    private int Dp(int r1, int c1, int c2) {
        int r2 = r1 + c1 - c2;
        if (r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1)
            return -1000000000;
        if (r1 == n - 1 && c1 == n - 1) return grid[r1][c1];
        if (memo[r1, c1, c2] != int.MinValue) return memo[r1, c1, c2];
        int cherries = grid[r1][c1];
        if (r1 != r2 || c1 != c2) cherries += grid[r2][c2];
        cherries += Math.Max(Math.Max(Dp(r1 + 1, c1, c2), Dp(r1, c1 + 1, c2)),
                             Math.Max(Dp(r1 + 1, c1, c2 + 1), Dp(r1, c1 + 1, c2 + 1)));
        return memo[r1, c1, c2] = cherries;
    }
}
