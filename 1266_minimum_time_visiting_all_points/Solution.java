// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int total = 0;
        for (int i = 1; i < points.length; i++) {
            total += Math.max(
                Math.abs(points[i][0] - points[i - 1][0]),
                Math.abs(points[i][1] - points[i - 1][1]));
        }
        return total;
    }
}
