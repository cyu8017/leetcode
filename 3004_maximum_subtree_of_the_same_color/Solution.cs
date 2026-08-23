// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumSubtreeSize(int[][] edges, int[] colors) {
        int n = edges.Length + 1;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] size = new int[n];
        int ans = 0;
        bool Dfs(int a, int fa) {
            size[a] = 1;
            bool ok = true;
            foreach (int b in g[a]) {
                if (b != fa) {
                    bool t = Dfs(b, a);
                    ok = ok && t && colors[a] == colors[b];
                    size[a] += size[b];
                }
            }
            if (ok) ans = Math.Max(ans, size[a]);
            return ok;
        }
        Dfs(0, -1);
        return ans;
    }
}
