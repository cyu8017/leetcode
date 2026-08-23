// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

using System;

public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long ans = 0;
        int n = bottomLeft.Length;
        for (int i = 0; i < n; i++) {
            int x1 = bottomLeft[i][0], y1 = bottomLeft[i][1];
            int x2 = topRight[i][0], y2 = topRight[i][1];
            for (int j = i + 1; j < n; j++) {
                int x3 = bottomLeft[j][0], y3 = bottomLeft[j][1];
                int x4 = topRight[j][0], y4 = topRight[j][1];
                int ww = Math.Min(x2, x4) - Math.Max(x1, x3);
                int h = Math.Min(y2, y4) - Math.Max(y1, y3);
                int e = Math.Min(ww, h);
                if (e > 0) ans = Math.Max(ans, (long)e * e);
            }
        }
        return ans;
    }
}
