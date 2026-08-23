// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int CollectTheCoins(int[] coins, int[][] edges) {
        int n = coins.Length;
        var g = new HashSet<int>[n];
        for (int i = 0; i < n; i++) g[i] = new HashSet<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] deg = new int[n];
        for (int i = 0; i < n; ++i) deg[i] = g[i].Count;
        var q = new Queue<int>();
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 1 && coins[i] == 0) q.Enqueue(i);
        }
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g[u].ToList()) {
                g[v].Remove(u);
                deg[v]--;
                if (deg[v] == 1 && coins[v] == 0) q.Enqueue(v);
            }
            g[u].Clear();
            deg[u] = 0;
        }
        for (int round = 0; round < 2; ++round) {
            var leaves = new List<int>();
            for (int i = 0; i < n; ++i) if (deg[i] == 1) leaves.Add(i);
            foreach (int u in leaves) {
                foreach (int v in g[u].ToList()) {
                    g[v].Remove(u);
                    deg[v]--;
                }
                g[u].Clear();
                deg[u] = 0;
            }
        }
        int remain = 0;
        for (int i = 0; i < n; ++i) remain += g[i].Count;
        return remain;
    }
}
