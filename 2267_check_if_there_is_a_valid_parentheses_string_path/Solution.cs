// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

using System.Collections.Generic;

public class Solution {
    int m, n;
    char[][] grid;
    HashSet<(int, int, int)> vis;

    bool Dfs(int r, int c, int bal) {
        if (r >= m || c >= n) return false;
        bal += (grid[r][c] == '(') ? 1 : -1;
        if (bal < 0) return false;
        if (r == m - 1 && c == n - 1) return bal == 0;
        var k = (r, c, bal);
        if (vis.Contains(k)) return false;
        vis.Add(k);
        return Dfs(r + 1, c, bal) || Dfs(r, c + 1, bal);
    }

    public bool HasValidPath(char[][] grid) {
        this.grid = grid;
        m = grid.Length; n = grid[0].Length;
        if ((m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;
        vis = new HashSet<(int, int, int)>();
        return Dfs(0, 0, 0);
    }
}
