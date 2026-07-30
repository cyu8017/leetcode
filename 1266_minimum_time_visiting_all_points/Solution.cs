// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

public class Solution {
    public int MinTimeToVisitAllPoints(int[][] points) {
        int total = 0;
        for (int i = 1; i < points.Length; i++) {
            total += System.Math.Max(
                System.Math.Abs(points[i][0] - points[i - 1][0]),
                System.Math.Abs(points[i][1] - points[i - 1][1]));
        }
        return total;
    }
}
