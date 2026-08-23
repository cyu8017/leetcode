// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTime(int n, int[][] relations, int[] time) {
        var g = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<int>();
        int[] indeg = new int[n + 1], dist = new int[n + 1];
        foreach (var e in relations) { g[e[0]].Add(e[1]); indeg[e[1]]++; }
        var q = new Queue<int>();
        for (int i = 1; i <= n; i++) {
            dist[i] = time[i - 1];
            if (indeg[i] == 0) q.Enqueue(i);
        }
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g[u]) {
                dist[v] = Math.Max(dist[v], dist[u] + time[v - 1]);
                if (--indeg[v] == 0) q.Enqueue(v);
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = Math.Max(ans, dist[i]);
        return ans;
    }
}
