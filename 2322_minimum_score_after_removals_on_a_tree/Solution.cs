// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumScore(int[] nums, int[][] edges) {
        int n = nums.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        int[] xorv = new int[n], inT = new int[n], outT = new int[n];
        int time = 0;
        void Dfs(int u, int p) {
            inT[u] = time++;
            xorv[u] = nums[u];
            foreach (int v in g[u]) if (v != p) { Dfs(v, u); xorv[u] ^= xorv[v]; }
            outT[u] = time;
        }
        Dfs(0, -1);
        bool IsAncestor(int a, int b) => inT[a] <= inT[b] && outT[b] <= outT[a];
        int total = xorv[0], ans = int.MaxValue;
        for (int i = 1; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int a, b, c;
                if (IsAncestor(i, j)) { a = xorv[j]; b = xorv[i] ^ xorv[j]; c = total ^ xorv[i]; }
                else if (IsAncestor(j, i)) { a = xorv[i]; b = xorv[j] ^ xorv[i]; c = total ^ xorv[j]; }
                else { a = xorv[i]; b = xorv[j]; c = total ^ xorv[i] ^ xorv[j]; }
                ans = Math.Min(ans, Math.Max(a, Math.Max(b, c)) - Math.Min(a, Math.Min(b, c)));
            }
        }
        return ans;
    }
}
