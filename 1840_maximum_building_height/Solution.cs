// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxBuilding(int n, int[][] restrictions) {
        var points = new List<int[]> { new[] { 1, 0 } };
        Array.Sort(restrictions, (a, b) => a[0].CompareTo(b[0]));
        foreach (var r in restrictions) points.Add(new[] { r[0], r[1] });
        if (points[^1][0] != n) points.Add(new[] { n, n - 1 });

        for (int i = 1; i < points.Count; i++) {
            int prevId = points[i - 1][0], prevH = points[i - 1][1];
            int currId = points[i][0], currH = points[i][1];
            points[i][1] = Math.Min(currH, prevH + currId - prevId);
        }
        for (int i = points.Count - 2; i >= 0; i--) {
            int nextId = points[i + 1][0], nextH = points[i + 1][1];
            int currId = points[i][0], currH = points[i][1];
            points[i][1] = Math.Min(currH, nextH + nextId - currId);
        }

        int best = 0;
        foreach (var p in points) best = Math.Max(best, p[1]);
        for (int i = 0; i < points.Count - 1; i++) {
            int id1 = points[i][0], h1 = points[i][1];
            int id2 = points[i + 1][0], h2 = points[i + 1][1];
            best = Math.Max(best, (h1 + h2 + id2 - id1) / 2);
        }
        return best;
    }
}
