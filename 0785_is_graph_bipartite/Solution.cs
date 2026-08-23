// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

public class Solution {
    private int[] color;

    public bool IsBipartite(int[][] graph) {
        color = new int[graph.Length];
        for (int i = 0; i < color.Length; i++) color[i] = -1;
        for (int node = 0; node < graph.Length; node++) {
            if (color[node] == -1 && !Dfs(graph, node, 0)) return false;
        }
        return true;
    }

    private bool Dfs(int[][] graph, int node, int c) {
        color[node] = c;
        foreach (int nei in graph[node]) {
            if (color[nei] == -1) {
                if (!Dfs(graph, nei, c ^ 1)) return false;
            } else if (color[nei] == c) return false;
        }
        return true;
    }
}
