// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

import java.util.*;

class Solution {
    private int time = 0;
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (List<Integer> e : connections) {
            graph[e.get(0)].add(e.get(1));
            graph[e.get(1)].add(e.get(0));
        }
        int[] disc = new int[n], low = new int[n];
        Arrays.fill(disc, -1);
        List<List<Integer>> bridges = new ArrayList<>();
        dfs(0, -1, graph, disc, low, bridges);
        for (List<Integer> b : bridges) {
            if (b.get(0) > b.get(1)) Collections.swap(b, 0, 1);
        }
        return bridges;
    }
    private void dfs(int node, int parent, List<Integer>[] graph, int[] disc, int[] low, List<List<Integer>> bridges) {
        disc[node] = low[node] = time++;
        for (int nxt : graph[node]) {
            if (nxt == parent) continue;
            if (disc[nxt] == -1) {
                dfs(nxt, node, graph, disc, low, bridges);
                low[node] = Math.min(low[node], low[nxt]);
                if (low[nxt] > disc[node]) bridges.add(new ArrayList<>(Arrays.asList(node, nxt)));
            } else low[node] = Math.min(low[node], disc[nxt]);
        }
    }
}
