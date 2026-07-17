// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

public class Solution {
    public int MinTrioDegree(int n, int[][] edges) {
        var adj = new bool[n, n];
        var degree = new int[n];
        foreach (var e in edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u, v] = true;
            adj[v, u] = true;
            degree[u]++;
            degree[v]++;
        }
        int best = int.MaxValue;
        foreach (var e in edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            for (int k = 0; k < n; k++) {
                if (adj[u, k] && adj[v, k]) {
                    best = System.Math.Min(best, degree[u] + degree[v] + degree[k] - 6);
                }
            }
        }
        return best == int.MaxValue ? -1 : best;
    }
}
