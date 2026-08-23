// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

using System;

public class Solution {
    public bool CanReachCorner(int xCorner, int yCorner, int[][] circles) {
        bool InCircle(int x, int y, int cx, int cy, int r) {
            long dx = x - cx, dy = y - cy;
            return dx * dx + dy * dy <= (long)r * r;
        }
        bool CrossLeftTop(int cx, int cy, int r) {
            bool a = Math.Abs(cx) <= r && cy >= 0 && cy <= yCorner;
            bool b = Math.Abs(cy - yCorner) <= r && cx >= 0 && cx <= xCorner;
            return a || b;
        }
        bool CrossRightBottom(int cx, int cy, int r) {
            bool a = Math.Abs(cx - xCorner) <= r && cy >= 0 && cy <= yCorner;
            bool b = Math.Abs(cy) <= r && cx >= 0 && cx <= xCorner;
            return a || b;
        }
        int n = circles.Length;
        bool[] vis = new bool[n];
        bool Dfs(int i) {
            int x1 = circles[i][0], y1 = circles[i][1], r1 = circles[i][2];
            if (CrossRightBottom(x1, y1, r1)) return true;
            vis[i] = true;
            for (int j = 0; j < n; j++) {
                if (vis[j]) continue;
                int x2 = circles[j][0], y2 = circles[j][1], r2 = circles[j][2];
                if ((long)(x1 - x2) * (x1 - x2) + (long)(y1 - y2) * (y1 - y2) > (long)(r1 + r2) * (r1 + r2)) continue;
                if ((long)x1 * r2 + (long)x2 * r1 < (long)(r1 + r2) * xCorner &&
                    (long)y1 * r2 + (long)y2 * r1 < (long)(r1 + r2) * yCorner && Dfs(j))
                    return true;
            }
            return false;
        }
        for (int i = 0; i < n; i++) {
            int x = circles[i][0], y = circles[i][1], r = circles[i][2];
            if (InCircle(0, 0, x, y, r) || InCircle(xCorner, yCorner, x, y, r)) return false;
            if (!vis[i] && CrossLeftTop(x, y, r) && Dfs(i)) return false;
        }
        return true;
    }
}
