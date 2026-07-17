// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int best = Integer.MAX_VALUE;
        int ans = -1;
        for (int i = 0; i < points.length; i++) {
            int px = points[i][0];
            int py = points[i][1];
            if (px != x && py != y) {
                continue;
            }
            int dist = Math.abs(px - x) + Math.abs(py - y);
            if (dist < best) {
                best = dist;
                ans = i;
            }
        }
        return ans;
    }
}
