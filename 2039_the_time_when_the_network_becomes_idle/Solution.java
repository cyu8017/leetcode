// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

import java.util.*;

class Solution {
    public int networkBecomesIdle(int[][] edges, int[] patience) {
        int n = patience.length;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]); }
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.offer(0); dist[0] = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g[u]) if (dist[v] == -1) { dist[v] = dist[u] + 1; q.offer(v); }
        }
        int ans = 0;
        for (int i = 1; i < n; i++) {
            int round = dist[i] * 2;
            int lastSend = (round - 1) / patience[i] * patience[i];
            ans = Math.max(ans, lastSend + round);
        }
        return ans + 1;
    }
}
