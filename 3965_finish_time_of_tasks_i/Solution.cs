// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

using System;
using System.Collections.Generic;

public class Solution {
    public long FinishTime(int n, int[][] edges, int[] baseTime) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) g[e[0]].Add(e[1]);
        long Dfs(int i) {
            if (g[i].Count == 0) return baseTime[i];
            const long INF = 1L << 62;
            long earliest = INF, latest = -INF;
            foreach (int j in g[i]) {
                long a = Dfs(j);
                earliest = Math.Min(earliest, a);
                latest = Math.Max(latest, a);
            }
            long ownDuration = (latest - earliest) + baseTime[i];
            return latest + ownDuration;
        }
        return Dfs(0);
    }
}
