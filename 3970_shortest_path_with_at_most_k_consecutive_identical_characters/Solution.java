// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public long shortestPath(int n, int[][] edges, String labels, int k) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] edge : edges) graph[edge[0]].add(new int[] { edge[1], edge[2] });
        final long infinity = Long.MAX_VALUE / 4;
        long[][] distances = new long[n][k + 1];
        for (int i = 0; i < n; i++) Arrays.fill(distances[i], infinity);
        distances[0][1] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[] { 0, 0, 1 });
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long distance = cur[0];
            int node = (int) cur[1], run = (int) cur[2];
            if (distance != distances[node][run]) continue;
            if (node == n - 1) return distance;
            for (int[] e : graph[node]) {
                int to = e[0], weight = e[1];
                int nextRun = 1;
                if (labels.charAt(node) == labels.charAt(to)) nextRun = run + 1;
                if (nextRun > k) continue;
                long nextDistance = distance + weight;
                if (nextDistance < distances[to][nextRun]) {
                    distances[to][nextRun] = nextDistance;
                    pq.offer(new long[] { nextDistance, to, nextRun });
                }
            }
        }
        return -1;
    }
}
