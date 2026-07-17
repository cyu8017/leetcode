// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int countRestrictedPaths(int n, int[][] edges) {
        List<int[]>[] adj = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            adj[e[0]].add(new int[] { e[1], e[2] });
            adj[e[1]].add(new int[] { e[0], e[2] });
        }
        long[] dist = new long[n + 1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[n] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>((p, q) -> Long.compare(p[0], q[0]));
        heap.add(new long[] { 0, n });
        while (!heap.isEmpty()) {
            long[] top = heap.poll();
            long d = top[0];
            int u = (int) top[1];
            if (d != dist[u]) {
                continue;
            }
            for (int[] vw : adj[u]) {
                long nd = d + vw[1];
                if (nd < dist[vw[0]]) {
                    dist[vw[0]] = nd;
                    heap.add(new long[] { nd, vw[0] });
                }
            }
        }
        Integer[] order = new Integer[n];
        for (int u = 1; u <= n; u++) {
            order[u - 1] = u;
        }
        Arrays.sort(order, (a, b) -> Long.compare(dist[a], dist[b]));
        long MOD = 1_000_000_007L;
        long[] cnt = new long[n + 1];
        cnt[n] = 1;
        for (int u : order) {
            if (u == n) {
                continue;
            }
            for (int[] vw : adj[u]) {
                if (dist[u] > dist[vw[0]]) {
                    cnt[u] = (cnt[u] + cnt[vw[0]]) % MOD;
                }
            }
        }
        return (int) cnt[1];
    }
}
