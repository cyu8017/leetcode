// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

class Solution {
    private int find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int[] findRedundantConnection(int[][] edges) {
        int[] parent = new int[edges.length + 1];
        for (int i = 0; i < parent.length; i++) parent[i] = i;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            int pu = find(parent, u), pv = find(parent, v);
            if (pu == pv) return new int[] {u, v};
            parent[pu] = pv;
        }
        return new int[0];
    }
}
