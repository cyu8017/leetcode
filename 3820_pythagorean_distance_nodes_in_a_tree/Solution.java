// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean_distance_nodes_in_a_tree/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

class Solution {
    private List<Integer>[] g;
    private int n;

    public int specialNodes(int n, int[][] edges, int x, int y, int z) {
        this.n = n;
        g = newList(n);
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] d1 = bfs(x), d2 = bfs(y), d3 = bfs(z);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int[] a = {d1[i], d2[i], d3[i]};
            Arrays.sort(a);
            long x0 = a[0], x1 = a[1], x2 = a[2];
            if (x0 * x0 + x1 * x1 == x2 * x2) ans++;
        }
        return ans;
    }

    private int[] bfs(int start) {
        int[] dist = new int[n];
        Arrays.fill(dist, 1_000_000_000);
        Queue<Integer> q = new ArrayDeque<>();
        dist[start] = 0;
        q.offer(start);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g[u]) {
                if (dist[v] > dist[u] + 1) {
                    dist[v] = dist[u] + 1;
                    q.offer(v);
                }
            }
        }
        return dist;
    }

    @SuppressWarnings("unchecked")
    private List<Integer>[] newList(int n) {
        List<Integer>[] g = (List<Integer>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
