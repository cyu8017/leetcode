// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

public class Solution {
    public int[] CountSubgraphsForEachDiameter(int n, int[][] edges) {
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0] - 1, b = e[1] - 1;
            adj[a].Add(b);
            adj[b].Add(a);
        }
        var ans = new int[n - 1];
        for (int mask = 1; mask < (1 << n); mask++) {
            if ((mask & (mask - 1)) == 0) continue;
            int start = BitOperations.TrailingZeroCount(mask);
            var (far, seen) = Bfs(adj, mask, start);
            if (seen.Count != BitOperations.PopCount((uint)mask)) continue;
            var (_, dist) = Bfs(adj, mask, far);
            ans[dist.Values.Max() - 1]++;
        }
        return ans;
    }

    private static (int far, Dictionary<int, int> dist) Bfs(List<int>[] adj, int mask, int src) {
        var dist = new Dictionary<int, int> { [src] = 0 };
        var q = new List<int> { src };
        for (int i = 0; i < q.Count; i++) {
            int u = q[i];
            foreach (int v in adj[u]) {
                if (((mask >> v) & 1) == 0 || dist.ContainsKey(v)) continue;
                dist[v] = dist[u] + 1;
                q.Add(v);
            }
        }
        int far = src;
        foreach (var kv in dist) if (kv.Value > dist[far]) far = kv.Key;
        return (far, dist);
    }
}
