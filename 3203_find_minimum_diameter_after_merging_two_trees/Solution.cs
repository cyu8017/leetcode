// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

using System;
using System.Collections.Generic;

public class Solution {
    int TreeDiameter(int[][] edges) {
        int n = edges.Length + 1;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int ans = 0, a = 0;
        void Dfs(int i, int fa, int t) {
            foreach (int j in g[i]) if (j != fa) Dfs(j, i, t + 1);
            if (ans < t) { ans = t; a = i; }
        }
        Dfs(0, -1, 0);
        Dfs(a, -1, 0);
        return ans;
    }

    public int MinimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        int d1 = TreeDiameter(edges1), d2 = TreeDiameter(edges2);
        return Math.Max(Math.Max(d1, d2), (d1 + 1) / 2 + (d2 + 1) / 2 + 1);
    }
}
