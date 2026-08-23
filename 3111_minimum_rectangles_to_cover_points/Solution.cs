// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

using System;

public class Solution {
    public int MinRectanglesToCoverPoints(int[][] points, int w) {
        Array.Sort(points, (a, b) => a[0].CompareTo(b[0]));
        int ans = 0, x1 = -1;
        foreach (var p in points) {
            if (p[0] > x1) {
                ans++;
                x1 = p[0] + w;
            }
        }
        return ans;
    }
}
