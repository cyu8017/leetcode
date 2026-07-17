// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

public class Solution {
    public int NearestValidPoint(int x, int y, int[][] points) {
        int best = int.MaxValue;
        int ans = -1;
        for (int i = 0; i < points.Length; i++) {
            int px = points[i][0];
            int py = points[i][1];
            if (px != x && py != y) {
                continue;
            }
            int dist = Math.Abs(px - x) + Math.Abs(py - y);
            if (dist < best) {
                best = dist;
                ans = i;
            }
        }
        return ans;
    }
}
