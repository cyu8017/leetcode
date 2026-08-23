// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

using System;

public class Solution {
    static int BitLen(uint x) {
        if (x == 0) return 0;
        int n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    }

    public int MinimumOR(int[][] grid) {
        int mx = 0;
        foreach (var row in grid) foreach (int x in row) mx = Math.Max(mx, x);
        int m = BitLen((uint)mx);
        int ans = 0;
        for (int i = m - 1; i >= 0; i--) {
            int mask = ans | ((1 << i) - 1);
            foreach (var row in grid) {
                bool found = false;
                foreach (int x in row) {
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
