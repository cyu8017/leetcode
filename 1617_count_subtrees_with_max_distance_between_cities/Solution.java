// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

import java.util.*;

class Solution {
    public int[] countSubgraphsForEachDiameter(int n, int[][] edges) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0] - 1, b = e[1] - 1;
            adj[a].add(b);
            adj[b].add(a);
        }
        int[] ans = new int[n - 1];
        for (int mask = 1; mask < (1 << n); mask++) {
            if ((mask & (mask - 1)) == 0) continue;
            int start = Integer.numberOfTrailingZeros(mask);
            int[] bfs1 = bfs(adj, mask, start);
            if (bfs1[0] != Integer.bitCount(mask)) continue;
            int[] bfs2 = bfs(adj, mask, bfs1[1]);
            ans[bfs2[2] - 1]++;
        }
        return ans;
    }

    // returns {seenCount, farthestNode, maxDist}
    private int[] bfs(List<Integer>[] adj, int mask, int src) {
        int[] dist = new int[adj.length];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(src);
        dist[src] = 0;
        int seen = 0, far = src, maxDist = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            seen++;
            if (dist[u] > maxDist) {
                maxDist = dist[u];
                far = u;
            }
            for (int v : adj[u]) {
                if (((mask >> v) & 1) == 1 && dist[v] < 0) {
                    dist[v] = dist[u] + 1;
                    q.offer(v);
                }
            }
        }
        return new int[] {seen, far, maxDist};
    }
}
