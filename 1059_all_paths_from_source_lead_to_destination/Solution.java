// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean leadsToDestination(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
        }
        int[] state = new int[n];
        return dfs(source, destination, graph, state);
    }

    private boolean dfs(int node, int destination, List<List<Integer>> graph, int[] state) {
        if (graph.get(node).isEmpty()) {
            return node == destination;
        }
        if (state[node] == 1) {
            return false;
        }
        if (state[node] == 2) {
            return true;
        }
        state[node] = 1;
        for (int nxt : graph.get(node)) {
            if (!dfs(nxt, destination, graph, state)) {
                return false;
            }
        }
        state[node] = 2;
        return true;
    }
}
