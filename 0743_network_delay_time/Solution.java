// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<int[]>[] graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();
        for (int[] edge : times) graph[edge[0]].add(new int[] {edge[1], edge[2]});
        final int INF = Integer.MAX_VALUE / 4;
        int[] dist = new int[n + 1];
        Arrays.fill(dist, INF);
        dist[k] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[] {0, k});
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int d = cur[0], node = cur[1];
            if (d > dist[node]) continue;
            for (int[] e : graph[node]) {
                int nd = d + e[1];
                if (nd < dist[e[0]]) {
                    dist[e[0]] = nd;
                    heap.offer(new int[] {nd, e[0]});
                }
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
        return ans == INF ? -1 : ans;
    }
}
