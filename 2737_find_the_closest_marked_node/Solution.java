// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;

class Solution {
    public int minimumDistance(int n, int[][] edges, int s, int[] marked) {
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) g[e[0]].add(new int[]{e[1], e[2]});
        Set<Integer> mark = new HashSet<>();
        for (int x : marked) mark.add(x);
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE / 4);
        dist[s] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[]{0, s});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (mark.contains(u)) return d;
            if (d > dist[u]) continue;
            for (int[] vw : g[u]) {
                int v = vw[0], w = vw[1];
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        return -1;
    }
}
