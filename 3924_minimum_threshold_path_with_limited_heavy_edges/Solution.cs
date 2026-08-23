// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

using System.Collections.Generic;

public class Solution {
    public int MinThreshold(int n, int[][] edges, int source, int target, int k) {
        if (source == target) return 0;
        var g = new List<(int to, int weight)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        int maxWeight = 0;
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
            if (e[2] > maxWeight) maxWeight = e[2];
        }
        bool Can(int threshold) {
            const int inf = 1000000000;
            int[] dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = inf;
            dist[source] = 0;
            var dq = new LinkedList<int>();
            dq.AddLast(source);
            while (dq.Count > 0) {
                int u = dq.First.Value;
                dq.RemoveFirst();
                foreach (var (to, weight) in g[u]) {
                    int cost = weight > threshold ? 1 : 0;
                    if (dist[u] + cost >= dist[to] || dist[u] + cost > k) continue;
                    dist[to] = dist[u] + cost;
                    if (cost == 0) dq.AddFirst(to);
                    else dq.AddLast(to);
                }
            }
            return dist[target] <= k;
        }
        if (!Can(maxWeight)) return -1;
        int lo = 0, hi = maxWeight;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
