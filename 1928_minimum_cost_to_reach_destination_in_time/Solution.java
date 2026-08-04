// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

import java.util.*;

class Solution {
    public int minCost(int maxTime, int[][] edges, int[] passingFee) {
        int n = passingFee.length;
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(new int[]{e[1], e[2]});
            graph[e[1]].add(new int[]{e[0], e[2]});
        }
        int[] minTime = new int[n];
        Arrays.fill(minTime, maxTime + 1);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{passingFee[0], 0, 0}); // cost, time, node
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int cost = cur[0], time = cur[1], u = cur[2];
            if (time >= minTime[u]) continue;
            minTime[u] = time;
            if (u == n - 1) return cost;
            for (int[] e : graph[u]) {
                int v = e[0], dt = e[1], nt = time + dt;
                if (nt <= maxTime && nt < minTime[v]) {
                    pq.offer(new int[]{cost + passingFee[v], nt, v});
                }
            }
        }
        return -1;
    }
}
