// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

using System.Collections.Generic;

public class Solution {
    private int[][] grid;
    private int m, n, target;
    private Dictionary<(int, int, int), bool> memo;

    public bool IsThereAPath(int[][] grid) {
        this.grid = grid;
        m = grid.Length;
        n = grid[0].Length;
        if ((m + n - 1) % 2 != 0) return false;
        target = (m + n - 1) / 2;
        memo = new Dictionary<(int, int, int), bool>();
        return Dfs(0, 0, 0);
    }

    private bool Dfs(int r, int c, int bal) {
        if (r >= m || c >= n) return false;
        bal += grid[r][c];
        if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false;
        if (r == m - 1 && c == n - 1) return bal == target;
        var key = (r, c, bal);
        if (memo.ContainsKey(key)) return memo[key];
        bool ok = Dfs(r + 1, c, bal) || Dfs(r, c + 1, bal);
        return memo[key] = ok;
    }
}
