// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

import java.util.HashSet;
import java.util.Set;

class Solution {
    private int m, n;
    private char[][] grid;
    private Set<Long> vis;

    private boolean dfs(int r, int c, int bal) {
        if (r >= m || c >= n) return false;
        bal += (grid[r][c] == '(') ? 1 : -1;
        if (bal < 0) return false;
        if (r == m - 1 && c == n - 1) return bal == 0;
        long k = (((long) r * n + c) << 10) | bal;
        if (!vis.add(k)) return false;
        return dfs(r + 1, c, bal) || dfs(r, c + 1, bal);
    }

    public boolean hasValidPath(char[][] grid) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        if ((m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;
        vis = new HashSet<>();
        return dfs(0, 0, 0);
    }
}
