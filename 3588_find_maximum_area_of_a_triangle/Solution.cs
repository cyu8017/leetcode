// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxArea(int[][] coords) {
        long Calc() {
            int mn = 1000000000, mx = 0;
            var f = new Dictionary<int, int>();
            var g = new Dictionary<int, int>();
            foreach (var c in coords) {
                int x = c[0], y = c[1];
                mn = Math.Min(mn, x);
                mx = Math.Max(mx, x);
                if (f.ContainsKey(x)) {
                    f[x] = Math.Min(f[x], y);
                    g[x] = Math.Max(g[x], y);
                } else {
                    f[x] = y;
                    g[x] = y;
                }
            }
            long ans = 0;
            foreach (var kv in f) {
                int x = kv.Key, y = kv.Value;
                int d = g[x] - y;
                ans = Math.Max(ans, 1L * d * Math.Max(mx - x, x - mn));
            }
            return ans;
        }
        long ans = Calc();
        foreach (var c in coords) { int t = c[0]; c[0] = c[1]; c[1] = t; }
        ans = Math.Max(ans, Calc());
        return ans > 0 ? ans : -1;
    }
}
