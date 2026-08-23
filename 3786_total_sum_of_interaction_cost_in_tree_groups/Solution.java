// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total_sum_of_interaction_cost_in_tree_groups/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long interactionCost(int n, int[][] edges, int[] group) {
        List<Integer>[] g = newList(n);
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] total = new int[21];
        for (int x : group) total[x]++;
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
        int[][] count = new int[n][21];
        long ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            int u = order.get(i);
            count[u][group[u]]++;
            for (int v : g[u]) {
                if (parent[v] != u) continue;
                for (int c = 1; c <= 20; c++) {
                    int x = count[v][c];
                    ans += (long) x * (total[c] - x);
                    count[u][c] += x;
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
