// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum_subgraph_score_in_a_tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] maxSubgraphScore(int n, int[][] edges, int[] good) {
        List<Integer>[] g = newList(n);
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] parent = new int[n];
        java.util.Arrays.fill(parent, -2);
        parent[0] = -1;
        List<Integer> order = new ArrayList<>();
        order.add(0);
        for (int i = 0; i < order.size(); i++) {
            int u = order.get(i);
            for (int v : g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.add(v);
                }
            }
        }
        int[] down = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int u = order.get(i);
            down[u] = 2 * good[u] - 1;
            for (int v : g[u]) {
                if (parent[v] == u && down[v] > 0) down[u] += down[v];
            }
        }
        int[] ans = down.clone();
        for (int u : order) {
            for (int v : g[u]) {
                if (parent[v] == u) {
                    int outside = ans[u];
                    if (down[v] > 0) outside -= down[v];
                    ans[v] = down[v];
                    if (outside > 0) ans[v] += outside;
                }
            }
        }
        return ans;
    }

    @SuppressWarnings("unchecked")
    private List<Integer>[] newList(int n) {
        List<Integer>[] g = (List<Integer>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
