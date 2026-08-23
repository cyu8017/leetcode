// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

import java.util.*;

class Solution {
    private int m, n, ans;
    private int[][] grid;
    private List<int[]> ones;

    private void dfs(int idx, int flips) {
        if (flips >= ans) return;
        while (idx < ones.size() && grid[ones.get(idx)[0]][ones.get(idx)[1]] == 0) idx++;
        if (idx == ones.size()) { ans = flips; return; }
        int r = ones.get(idx)[0], c = ones.get(idx)[1];
        List<int[]> changed = new ArrayList<>();
        for (int j = 0; j < n; j++) if (grid[r][j] == 1) { grid[r][j] = 0; changed.add(new int[] {r, j}); }
        dfs(idx + 1, flips + 1);
        for (int[] p : changed) grid[p[0]][p[1]] = 1;
        changed.clear();
        for (int i = 0; i < m; i++) if (grid[i][c] == 1) { grid[i][c] = 0; changed.add(new int[] {i, c}); }
        dfs(idx + 1, flips + 1);
        for (int[] p : changed) grid[p[0]][p[1]] = 1;
    }

    public int removeOnes(int[][] grid) {
        this.grid = grid;
        m = grid.length; n = grid[0].length;
        ones = new ArrayList<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) ones.add(new int[] {i, j});
        if (ones.isEmpty()) return 0;
        ans = m + n;
        dfs(0, 0);
        return ans;
    }
}
