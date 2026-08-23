// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

class Solution {
    public int minThreshold(int n, int[][] edges, int source, int target, int k) {
        if (source == target) return 0;
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        int maxWeight = 0;
        for (int[] e : edges) {
            g[e[0]].add(new int[] { e[1], e[2] });
            g[e[1]].add(new int[] { e[0], e[2] });
            maxWeight = Math.max(maxWeight, e[2]);
        }
        if (!can(n, g, source, target, k, maxWeight)) return -1;
        int lo = 0, hi = maxWeight;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (can(n, g, source, target, k, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean can(int n, List<int[]>[] g, int source, int target, int k, int threshold) {
        final int inf = 1000000000;
        int[] dist = new int[n];
        Arrays.fill(dist, inf);
        dist[source] = 0;
        Deque<Integer> dq = new ArrayDeque<>();
        dq.addLast(source);
        while (!dq.isEmpty()) {
            int u = dq.pollFirst();
            for (int[] e : g[u]) {
                int to = e[0], weight = e[1];
                int cost = weight > threshold ? 1 : 0;
                if (dist[u] + cost >= dist[to] || dist[u] + cost > k) continue;
                dist[to] = dist[u] + cost;
                if (cost == 0) dq.addFirst(to);
                else dq.addLast(to);
            }
        }
        return dist[target] <= k;
    }
}
