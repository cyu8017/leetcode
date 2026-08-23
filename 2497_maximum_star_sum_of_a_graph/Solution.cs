// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxStarSum(int[] vals, int[][] edges, int k) {
        int n = vals.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int ans = vals[0];
        for (int i = 0; i < n; i++) {
            var neigh = new List<int>();
            foreach (int v in g[i]) {
                if (vals[v] > 0) neigh.Add(vals[v]);
            }
            neigh.Sort((a, b) => b.CompareTo(a));
            int sum = vals[i];
            for (int j = 0; j < neigh.Count && j < k; j++) sum += neigh[j];
            if (sum > ans) ans = sum;
        }
        return ans;
    }
}
