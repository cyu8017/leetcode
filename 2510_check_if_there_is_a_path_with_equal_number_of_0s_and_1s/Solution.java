// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[][] grid;
    private int m, n, target;
    private Map<Long, Boolean> memo;

    private long key(int r, int c, int bal) {
        return (((long) r) << 40) | (((long) c) << 20) | (bal & 0xfffffL);
    }

    private boolean dfs(int r, int c, int bal) {
        if (r >= m || c >= n) return false;
        bal += grid[r][c];
        if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false;
        if (r == m - 1 && c == n - 1) return bal == target;
        long k = key(r, c, bal);
        Boolean cached = memo.get(k);
        if (cached != null) return cached;
        boolean ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal);
        memo.put(k, ok);
        return ok;
    }

    public boolean isThereAPath(int[][] grid) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        if ((m + n - 1) % 2 != 0) return false;
        target = (m + n - 1) / 2;
        memo = new HashMap<>();
        return dfs(0, 0, 0);
    }
}
