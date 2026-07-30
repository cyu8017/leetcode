// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        int[] parent = new int[n + 1];
        for (int i = 0; i <= n; i++) parent[i] = i;

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        var edges = new List<int[]>();
        for (int i = 0; i < wells.Length; i++) {
            edges.Add(new[] { 0, i + 1, wells[i] });
        }
        foreach (var p in pipes) edges.Add(p);
        edges.Sort((a, b) => a[2].CompareTo(b[2]));

        int ans = 0;
        foreach (var e in edges) {
            int ra = Find(e[0]), rb = Find(e[1]);
            if (ra == rb) continue;
            parent[rb] = ra;
            ans += e[2];
        }
        return ans;
    }
}
