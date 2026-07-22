// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        var degree = new int[n];
        var edges = new HashSet<(int, int)>();
        foreach (var road in roads) {
            int a = road[0], b = road[1];
            degree[a]++;
            degree[b]++;
            edges.Add((Math.Min(a, b), Math.Max(a, b)));
        }
        int ans = 0;
        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                int rank = degree[a] + degree[b] - (edges.Contains((a, b)) ? 1 : 0);
                ans = Math.Max(ans, rank);
            }
        }
        return ans;
    }
}
