// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

public class Solution {
    public bool ValidTree(int n, int[][] edges) {
        if (edges.Length != n - 1) {
            return false;
        }
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        foreach (int[] edge in edges) {
            int rootLeft = Find(parent, edge[0]);
            int rootRight = Find(parent, edge[1]);
            if (rootLeft == rootRight) {
                return false;
            }
            parent[rootLeft] = rootRight;
        }
        return true;
    }

    private int Find(int[] parent, int node) {
        if (parent[node] != node) {
            parent[node] = Find(parent, parent[node]);
        }
        return parent[node];
    }
}
