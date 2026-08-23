// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

using System.Collections.Generic;

public class Solution {
    public int MinScore(int n, int[][] roads) {
        var g = new List<(int v, int w)>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<(int, int)>();
        foreach (var r in roads) {
            g[r[0]].Add((r[1], r[2]));
            g[r[1]].Add((r[0], r[2]));
        }
        bool[] vis = new bool[n + 1];
        int ans = 1 << 30;
        var q = new Queue<int>();
        q.Enqueue(1);
        vis[1] = true;
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (var (v, w) in g[u]) {
                if (w < ans) ans = w;
                if (!vis[v]) {
                    vis[v] = true;
                    q.Enqueue(v);
                }
            }
        }
        return ans;
    }
}
