// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

using System.Collections.Generic;

public class Solution {
    public int ReachableNodes(int n, int[][] edges, int[] restricted) {
        var ban = new HashSet<int>(restricted);
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        int ans = 0;
        bool[] vis = new bool[n];
        var q = new Queue<int>();
        q.Enqueue(0);
        vis[0] = true;
        while (q.Count > 0) {
            int u = q.Dequeue();
            ans++;
            foreach (int v in g[u]) {
                if (!vis[v] && !ban.Contains(v)) {
                    vis[v] = true;
                    q.Enqueue(v);
                }
            }
        }
        return ans;
    }
}
