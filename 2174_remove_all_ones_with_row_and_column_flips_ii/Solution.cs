// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

public class Solution {
    public int RemoveOnes(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var ones = new List<(int r, int c)>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) ones.Add((i, j));
        if (ones.Count == 0) return 0;
        int ans = m + n;
        void Dfs(int idx, int flips) {
            if (flips >= ans) return;
            while (idx < ones.Count && grid[ones[idx].r][ones[idx].c] == 0) idx++;
            if (idx == ones.Count) { ans = flips; return; }
            int r = ones[idx].r, c = ones[idx].c;
            var changed = new List<(int r, int c)>();
            for (int j = 0; j < n; j++) if (grid[r][j] == 1) { grid[r][j] = 0; changed.Add((r, j)); }
            Dfs(idx + 1, flips + 1);
            foreach (var p in changed) grid[p.r][p.c] = 1;
            changed.Clear();
            for (int i = 0; i < m; i++) if (grid[i][c] == 1) { grid[i][c] = 0; changed.Add((i, c)); }
            Dfs(idx + 1, flips + 1);
            foreach (var p in changed) grid[p.r][p.c] = 1;
        }
        Dfs(0, 0);
        return ans;
    }
}
