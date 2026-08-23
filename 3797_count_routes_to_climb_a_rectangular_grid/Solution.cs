// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

using System;

public class Solution {
    public int CountRoutes(string[] grid, int d) {
        const int MOD = 1000000007;
        int n = grid.Length, m = grid[0].Length;
        int upRadius = 0;
        while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) upRadius++;
        int[] arrived = new int[m];
        for (int c = 0; c < m; c++) {
            if (grid[n - 1][c] == '.') arrived[c] = 1;
        }
        (int[] bas, int[] horizontal) RowWays(int row, int[] basArr) {
            int[] pref = new int[m + 1];
            for (int i = 0; i < m; i++) pref[i + 1] = (pref[i] + basArr[i]) % MOD;
            int[] horizontal = new int[m];
            for (int c = 0; c < m; c++) {
                if (grid[row][c] == '#') continue;
                int l = Math.Max(0, c - d), r = Math.Min(m - 1, c + d);
                horizontal[c] = (pref[r + 1] - pref[l] - basArr[c]) % MOD;
                if (horizontal[c] < 0) horizontal[c] += MOD;
            }
            return (basArr, horizontal);
        }
        for (int r = n - 1; r >= 0; r--) {
            var (bas, horizontal) = RowWays(r, arrived);
            if (r == 0) {
                int ans = 0;
                for (int c = 0; c < m; c++) ans = (ans + bas[c] + horizontal[c]) % MOD;
                return ans;
            }
            int[] pref = new int[m + 1];
            for (int c = 0; c < m; c++) pref[c + 1] = (pref[c] + bas[c] + horizontal[c]) % MOD;
            int[] next = new int[m];
            for (int c = 0; c < m; c++) {
                if (grid[r - 1][c] == '#') continue;
                int l = Math.Max(0, c - upRadius), rr = Math.Min(m - 1, c + upRadius);
                next[c] = pref[rr + 1] - pref[l];
                if (next[c] < 0) next[c] += MOD;
            }
            arrived = next;
        }
        return 0;
    }
}
