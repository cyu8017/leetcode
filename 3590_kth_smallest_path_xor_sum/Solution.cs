// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] KthSmallest(int[] par, int[] vals, int[][] queries) {
        int n = par.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 1; i < n; i++) g[par[i]].Add(i);
        int[] xorPath = new int[n];
        void Dfs(int u) {
            xorPath[u] ^= vals[u];
            foreach (int v in g[u]) {
                xorPath[v] = xorPath[u];
                Dfs(v);
            }
        }
        Dfs(0);
        int[] inT = new int[n], outT = new int[n];
        var order = new List<int>();
        void Dfs2(int u) {
            inT[u] = order.Count;
            order.Add(xorPath[u]);
            foreach (int v in g[u]) Dfs2(v);
            outT[u] = order.Count;
        }
        Dfs2(0);
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int u = queries[i][0], k = queries[i][1];
            var sub = order.GetRange(inT[u], outT[u] - inT[u]);
            sub.Sort();
            var uniq = new List<int>();
            foreach (int x in sub) if (uniq.Count == 0 || uniq[uniq.Count - 1] != x) uniq.Add(x);
            ans[i] = k > uniq.Count ? -1 : uniq[k - 1];
        }
        return ans;
    }
}
