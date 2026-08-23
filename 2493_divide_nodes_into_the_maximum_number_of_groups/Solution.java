// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

class Solution {
    private List<Integer>[] g;
    private int n;

    private int bfsDepth(int start) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(start);
        dist[start] = 1;
        int best = 1;
        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > best) best = dist[u];
            for (int v : g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.offer(v);
                }
            }
        }
        return best;
    }

    public int magnificentSets(int n, int[][] edges) {
        this.n = n;
        g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] color = new int[n + 1];
        Arrays.fill(color, -1);
        List<List<Integer>> components = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (color[i] != -1) continue;
            List<Integer> comp = new ArrayList<>();
            Queue<Integer> q = new ArrayDeque<>();
            q.offer(i);
            color[i] = 0;
            boolean bipartite = true;
            while (!q.isEmpty()) {
                int u = q.poll();
                comp.add(u);
                for (int v : g[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        q.offer(v);
                    } else if (color[v] == color[u]) {
                        bipartite = false;
                    }
                }
            }
            if (!bipartite) return -1;
            components.add(comp);
        }
        int ans = 0;
        for (List<Integer> comp : components) {
            int best = 0;
            for (int u : comp) best = Math.max(best, bfsDepth(u));
            ans += best;
        }
        return ans;
    }
}
