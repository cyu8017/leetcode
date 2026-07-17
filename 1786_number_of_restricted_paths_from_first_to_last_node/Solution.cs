// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

public class Solution {
    public int CountRestrictedPaths(int n, int[][] edges) {
        var adj = new List<int[]>[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new List<int[]>();
        }
        foreach (var e in edges) {
            adj[e[0]].Add(new int[] { e[1], e[2] });
            adj[e[1]].Add(new int[] { e[0], e[2] });
        }
        var dist = new long[n + 1];
        Array.Fill(dist, long.MaxValue);
        dist[n] = 0;
        var heap = new PriorityQueue<int, long>();
        heap.Enqueue(n, 0);
        while (heap.TryDequeue(out int u, out long d)) {
            if (d != dist[u]) {
                continue;
            }
            foreach (var vw in adj[u]) {
                long nd = d + vw[1];
                if (nd < dist[vw[0]]) {
                    dist[vw[0]] = nd;
                    heap.Enqueue(vw[0], nd);
                }
            }
        }
        var order = new int[n];
        for (int i = 0; i < n; i++) {
            order[i] = i + 1;
        }
        Array.Sort(order, (a, b) => dist[a].CompareTo(dist[b]));
        const long MOD = 1000000007;
        var cnt = new long[n + 1];
        cnt[n] = 1;
        foreach (int u in order) {
            if (u == n) {
                continue;
            }
            foreach (var vw in adj[u]) {
                if (dist[u] > dist[vw[0]]) {
                    cnt[u] = (cnt[u] + cnt[vw[0]]) % MOD;
                }
            }
        }
        return (int)cnt[1];
    }
}
