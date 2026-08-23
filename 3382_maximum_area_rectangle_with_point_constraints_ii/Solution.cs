// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.Length;
        int[][] points = new int[n][];
        for (int i = 0; i < n; i++) points[i] = new int[] { xCoord[i], yCoord[i] };
        var set = new HashSet<(int, int)>();
        foreach (var p in points) set.Add((p[0], p[1]));
        long ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue;
                if (!set.Contains((x1, y2)) || !set.Contains((x2, y1))) continue;
                int minX = Math.Min(x1, x2), maxX = Math.Max(x1, x2);
                int minY = Math.Min(y1, y2), maxY = Math.Max(y1, y2);
                bool ok = true;
                foreach (var p in points) {
                    int x = p[0], y = p[1];
                    if (x > minX && x < maxX && y > minY && y < maxY) { ok = false; break; }
                    bool onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                                    ((y == minY || y == maxY) && x >= minX && x <= maxX);
                    if (onBorder) {
                        bool isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                        if (!isCorner) { ok = false; break; }
                    }
                }
                if (ok) {
                    long area = (long)(maxX - minX) * (maxY - minY);
                    if (area > ans) ans = area;
                }
            }
        }
        return ans;
    }
}
