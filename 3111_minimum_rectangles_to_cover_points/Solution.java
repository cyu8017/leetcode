// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

import java.util.Arrays;

class Solution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        int ans = 0, x1 = -1;
        for (int[] p : points) {
            if (p[0] > x1) {
                ans++;
                x1 = p[0] + w;
            }
        }
        return ans;
    }
}
