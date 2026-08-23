// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

using System.Collections.Generic;

public class Solution {
    public int CountCompleteComponents(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        bool[] vis = new bool[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            var nodes = new List<int>();
            void Dfs(int u) {
                vis[u] = true; nodes.Add(u);
                foreach (int v in g[u]) if (!vis[v]) Dfs(v);
            }
            Dfs(i);
            int ecount = 0;
            foreach (int u in nodes) ecount += g[u].Count;
            ecount /= 2;
            int sz = nodes.Count;
            if (ecount == sz * (sz - 1) / 2) ans++;
        }
        return ans;
    }
}
