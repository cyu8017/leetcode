// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

public class Solution {
    private int Find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int[] FindRedundantConnection(int[][] edges) {
        int[] parent = new int[edges.Length + 1];
        for (int i = 0; i < parent.Length; i++) parent[i] = i;
        foreach (var edge in edges) {
            int u = edge[0], v = edge[1];
            int pu = Find(parent, u), pv = Find(parent, v);
            if (pu == pv) return new[] { u, v };
            parent[pu] = pv;
        }
        return System.Array.Empty<int>();
    }
}
