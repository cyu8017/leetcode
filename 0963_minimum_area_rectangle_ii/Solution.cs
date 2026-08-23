// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public double MinAreaFreeRect(int[][] points) {
        int n = points.Length;
        var groups = new Dictionary<(long cx, long cy, long dist), List<(int, int)>>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long cx = points[i][0] + points[j][0];
                long cy = points[i][1] + points[j][1];
                long dx = points[i][0] - points[j][0];
                long dy = points[i][1] - points[j][1];
                long dist = dx * dx + dy * dy;
                var key = (cx, cy, dist);
                if (!groups.ContainsKey(key)) groups[key] = new List<(int, int)>();
                groups[key].Add((i, j));
            }
        }
        double ans = 1e300;
        foreach (var pairs in groups.Values) {
            for (int a = 0; a < pairs.Count; a++) {
                for (int b = a + 1; b < pairs.Count; b++) {
                    int p1 = pairs[a].Item1, p2 = pairs[b].Item1, q2 = pairs[b].Item2;
                    double d1 = Math.Hypot(points[p1][0] - points[p2][0], points[p1][1] - points[p2][1]);
                    double d2 = Math.Hypot(points[p1][0] - points[q2][0], points[p1][1] - points[q2][1]);
                    double area = d1 * d2;
                    if (area > 0) ans = Math.Min(ans, area);
                }
            }
        }
        return ans >= 1e299 ? 0.0 : ans;
    }
}
