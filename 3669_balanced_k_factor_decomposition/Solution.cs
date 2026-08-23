// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

using System;
using System.Collections.Generic;

public class Solution {
    const int MX = 100001;
    static List<int>[] g;
    static bool inited;
    int cur;
    int[] ans, path;

    static void EnsureInit() {
        if (inited) return;
        g = new List<int>[MX];
        for (int i = 0; i < MX; i++) g[i] = new List<int>();
        for (int i = 1; i < MX; i++) {
            for (int j = i; j < MX; j += i) g[j].Add(i);
        }
        inited = true;
    }

    void Dfs(int i, int x, int mi, int mx) {
        if (i == 0) {
            int d = Math.Max(mx, x) - Math.Min(mi, x);
            if (d < cur) {
                cur = d;
                path[i] = x;
                ans = (int[])path.Clone();
            }
            return;
        }
        foreach (int y in g[x]) {
            path[i] = y;
            Dfs(i - 1, x / y, Math.Min(mi, y), Math.Max(mx, y));
        }
    }

    public int[] MinDifference(int n, int k) {
        EnsureInit();
        cur = int.MaxValue;
        ans = Array.Empty<int>();
        path = new int[k];
        Dfs(k - 1, n, int.MaxValue, 0);
        return ans;
    }
}
