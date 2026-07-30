// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

using System;
using System.Collections.Generic;

public class Solution {
    const int MOD = 1000000007;
    Dictionary<(int, int), int> memo;
    List<int> states;
    Dictionary<int, List<int>> compat;
    int n;

    public int ColorTheGrid(int m, int n) {
        this.n = n;
        states = new List<int>();
        int total = (int)Math.Pow(3, m);
        for (int s = 0; s < total; s++)
            if (ValidColumn(s, m)) states.Add(s);
        compat = new Dictionary<int, List<int>>();
        foreach (int a in states) {
            compat[a] = new List<int>();
            var ca = GetColors(a, m);
            foreach (int b in states) {
                var cb = GetColors(b, m);
                bool ok = true;
                for (int i = 0; i < m; i++) if (ca[i] == cb[i]) { ok = false; break; }
                if (ok) compat[a].Add(b);
            }
        }
        memo = new Dictionary<(int, int), int>();
        return Dp(0, -1);
    }

    bool ValidColumn(int mask, int m) {
        int prev = -1;
        for (int i = 0; i < m; i++) {
            int c = mask % 3;
            if (c == prev) return false;
            prev = c;
            mask /= 3;
        }
        return true;
    }

    int[] GetColors(int mask, int m) {
        var cols = new int[m];
        for (int i = 0; i < m; i++) {
            cols[i] = mask % 3;
            mask /= 3;
        }
        return cols;
    }

    int Dp(int col, int prev) {
        if (col == n) return 1;
        if (memo.TryGetValue((col, prev), out int cached)) return cached;
        int total = 0;
        var cands = prev == -1 ? states : compat[prev];
        foreach (int cur in cands)
            total = (total + Dp(col + 1, cur)) % MOD;
        return memo[(col, prev)] = total;
    }
}