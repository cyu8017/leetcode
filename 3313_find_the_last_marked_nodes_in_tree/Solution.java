// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

class Solution {
    private List<Integer>[] g;
    private int n;

    /** @return {farthestNode, dist[]} */
    private Object[] bfs(int start) {
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(start);
        dist[start] = 0;
        int far = start;
        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > dist[far]) far = u;
            for (int v : g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.offer(v);
                }
            }
        }
        return new Object[] {far, dist};
    }

    public int[] lastMarkedNodes(int[][] edges) {
        n = edges.length + 1;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        Object[] r0 = bfs(0);
        int u = (Integer) r0[0];
        Object[] ru = bfs(u);
        int v = (Integer) ru[0];
        int[] du = (int[]) ru[1];
        Object[] rv = bfs(v);
        int[] dv = (int[]) rv[1];
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = du[i] >= dv[i] ? u : v;
        return ans;
    }
}
