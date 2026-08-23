// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

import java.util.*;

class Solution {
    public int minimumCost(int[] start, int[] target, int[][] specialRoads) {
        List<int[]> points = new ArrayList<>();
        points.add(start);
        points.add(target);
        for (int[] r : specialRoads) {
            points.add(new int[] {r[0], r[1]});
            points.add(new int[] {r[2], r[3]});
        }
        int N = points.size();
        List<int[]>[] g = new List[N];
        for (int i = 0; i < N; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (i != j) g[i].add(new int[] {j, man(points.get(i), points.get(j))});
        for (int[] r : specialRoads) {
            int u = -1, v = -1;
            for (int i = 0; i < N; i++) {
                int[] p = points.get(i);
                if (p[0] == r[0] && p[1] == r[1]) u = i;
                if (p[0] == r[2] && p[1] == r[3]) v = i;
            }
            if (u >= 0 && v >= 0) g[u].add(new int[] {v, r[4]});
        }
        int[] dist = new int[N];
        Arrays.fill(dist, Integer.MAX_VALUE / 4);
        dist[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[] {0, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int id = cur[0], cost = cur[1];
            if (cost > dist[id]) continue;
            for (int[] e : g[id]) {
                if (cost + e[1] < dist[e[0]]) {
                    dist[e[0]] = cost + e[1];
                    pq.offer(new int[] {e[0], dist[e[0]]});
                }
            }
        }
        return dist[1];
    }

    private int man(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
}
