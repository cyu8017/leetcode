// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

class Solution {
    static int bitLen(int x) {
        if (x == 0) return 0;
        int n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    }

    public int minimumOR(int[][] grid) {
        int mx = 0;
        for (var row : grid.entrySet()) for (int x : row) mx = Math.max(mx, x);
        int m = bitLen((int)mx);
        int ans = 0;
        for (int i = m - 1; i >= 0; i--) {
            int mask = ans | ((1 << i) - 1);
            for (var row : grid.entrySet()) {
                boolean found = false;
                for (int x : row) {
                    if ((x | mask) == mask) { found = true; break; }
                }
                if (!found) {
                    ans |= 1 << i;
                    break;
                }
            }
        }
        return ans;
    }
}
