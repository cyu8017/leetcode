// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count_routes_to_climb_a_rectangular_grid/

class Solution {
    public int countRoutes(String[] grid, int d) {
        final int MOD = 1_000_000_007;
        int n = grid.length, m = grid[0].length();
        int upRadius = 0;
        while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) upRadius++;
        int[] arrived = new int[m];
        for (int c = 0; c < m; c++) {
            if (grid[n - 1].charAt(c) == '.') arrived[c] = 1;
        }
        for (int r = n - 1; r >= 0; r--) {
            int[] pref = new int[m + 1];
            for (int i = 0; i < m; i++) pref[i + 1] = (pref[i] + arrived[i]) % MOD;
            int[] horizontal = new int[m];
            for (int c = 0; c < m; c++) {
                if (grid[r].charAt(c) == '#') continue;
                int l = Math.max(0, c - d), rr = Math.min(m - 1, c + d);
                horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % MOD;
                if (horizontal[c] < 0) horizontal[c] += MOD;
            }
            if (r == 0) {
                int ans = 0;
                for (int c = 0; c < m; c++) ans = (ans + arrived[c] + horizontal[c]) % MOD;
                return ans;
            }
            int[] pref2 = new int[m + 1];
            for (int c = 0; c < m; c++) pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % MOD;
            int[] next = new int[m];
            for (int c = 0; c < m; c++) {
                if (grid[r - 1].charAt(c) == '#') continue;
                int l = Math.max(0, c - upRadius), rr = Math.min(m - 1, c + upRadius);
                next[c] = pref2[rr + 1] - pref2[l];
                if (next[c] < 0) next[c] += MOD;
            }
            arrived = next;
        }
        return 0;
    }
}
