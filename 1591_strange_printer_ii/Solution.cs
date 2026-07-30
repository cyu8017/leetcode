// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public bool IsPrintable(int[][] targetGrid) {
        var colors = new HashSet<int>();
        int m = targetGrid.Length, n = targetGrid[0].Length;
        foreach (var row in targetGrid)
            foreach (int x in row) colors.Add(x);

        var bounds = new Dictionary<int, int[]>();
        foreach (int c in colors) bounds[c] = new[] { int.MaxValue, int.MaxValue, -1, -1 };
        for (int r = 0; r < m; r++) {
            for (int col = 0; col < n; col++) {
                int c = targetGrid[r][col];
                var b = bounds[c];
                b[0] = Math.Min(b[0], r);
                b[1] = Math.Min(b[1], col);
                b[2] = Math.Max(b[2], r);
                b[3] = Math.Max(b[3], col);
            }
        }

        var graph = new Dictionary<int, HashSet<int>>();
        var indegree = new Dictionary<int, int>();
        foreach (int c in colors) {
            graph[c] = new HashSet<int>();
            indegree[c] = 0;
        }
        foreach (var kv in bounds) {
            int c = kv.Key;
            var b = kv.Value;
            for (int r = b[0]; r <= b[2]; r++) {
                for (int col = b[1]; col <= b[3]; col++) {
                    int other = targetGrid[r][col];
                    if (other != c && graph[c].Add(other)) indegree[other]++;
                }
            }
        }

        var queue = new Queue<int>();
        foreach (int c in colors)
            if (indegree[c] == 0) queue.Enqueue(c);
        int seen = 0;
        while (queue.Count > 0) {
            int c = queue.Dequeue();
            seen++;
            foreach (int nxt in graph[c]) {
                indegree[nxt]--;
                if (indegree[nxt] == 0) queue.Enqueue(nxt);
            }
        }
        return seen == colors.Count;
    }
}
