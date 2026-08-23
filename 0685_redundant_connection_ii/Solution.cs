// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

using System.Collections.Generic;

public class Solution {
    private int Find(int[] uf, int x) {
        while (uf[x] != x) {
            uf[x] = uf[uf[x]];
            x = uf[x];
        }
        return x;
    }

    public int[] FindRedundantDirectedConnection(int[][] edges) {
        int n = edges.Length;
        int[] parent = new int[n + 1];
        int[] cand1 = null, cand2 = null;
        for (int i = 0; i < n; i++) {
            int u = edges[i][0], v = edges[i][1];
            if (parent[v] == 0) parent[v] = u;
            else {
                cand1 = new[] { parent[v], v };
                cand2 = new[] { u, v };
                edges[i] = new[] { -1, -1 };
                break;
            }
        }
        int[] uf = new int[n + 1];
        for (int i = 0; i <= n; i++) uf[i] = i;
        foreach (var edge in edges) {
            if (edge[0] < 0) continue;
            int pu = Find(uf, edge[0]), pv = Find(uf, edge[1]);
            if (pu == pv) return cand1 ?? new[] { edge[0], edge[1] };
            uf[pu] = pv;
        }
        return cand2;
    }
}
