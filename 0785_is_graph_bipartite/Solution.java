// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

class Solution {
    private int[] color;

    public boolean isBipartite(int[][] graph) {
        color = new int[graph.length];
        java.util.Arrays.fill(color, -1);
        for (int node = 0; node < graph.length; node++) {
            if (color[node] == -1 && !dfs(graph, node, 0)) return false;
        }
        return true;
    }

    private boolean dfs(int[][] graph, int node, int c) {
        color[node] = c;
        for (int nei : graph[node]) {
            if (color[nei] == -1) {
                if (!dfs(graph, nei, c ^ 1)) return false;
            } else if (color[nei] == c) {
                return false;
            }
        }
        return true;
    }
}
