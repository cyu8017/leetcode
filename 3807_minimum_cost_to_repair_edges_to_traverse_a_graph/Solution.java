// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum_cost_to_repair_edges_to_traverse_a_graph/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int[][] edges;
    private int n, k;

    public int minCost(int n, int[][] edges, int k) {
        this.n = n;
        this.k = k;
        this.edges = edges;
        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));
        int m = edges.length;
        if (m == 0) return -1;
        int l = 0, r = m - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(mid)) r = mid;
            else l = mid + 1;
        }
        if (check(l)) return edges[l][2];
        return -1;
    }

    private boolean check(int idx) {
        List<Integer>[] g = newList(n);
        for (int i = 0; i <= idx; i++) {
            g[edges[i][0]].add(edges[i][1]);
            g[edges[i][1]].add(edges[i][0]);
        }
        List<Integer> q = new ArrayList<>();
        q.add(0);
        boolean[] vis = new boolean[n];
        vis[0] = true;
        int dist = 0;
        while (!q.isEmpty()) {
            List<Integer> nq = new ArrayList<>();
            for (int u : q) {
                if (u == n - 1) return dist <= k;
                for (int v : g[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        nq.add(v);
                    }
                }
            }
            q = nq;
            dist++;
        }
        return false;
    }

    @SuppressWarnings("unchecked")
    private List<Integer>[] newList(int n) {
        List<Integer>[] g = (List<Integer>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
