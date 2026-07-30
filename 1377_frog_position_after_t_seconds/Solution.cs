// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

using System.Collections.Generic;
public class Solution {
    public double FrogPosition(int n, int[][] edges, int t, int target) {
        var g = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        double Dfs(int u, int p, int time, double prob) {
            var kids = new List<int>();
            foreach (int v in g[u]) if (v != p) kids.Add(v);
            if (time == t || kids.Count == 0) return u == target ? prob : 0;
            double sum = 0;
            foreach (int v in kids) sum += Dfs(v, u, time + 1, prob / kids.Count);
            return sum;
        }
        return Dfs(1, 0, 0, 1.0);
    }
}
