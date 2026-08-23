// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long ans = 0;
        int n = bottomLeft.length;
        for (int i = 0; i < n; i++) {
            int x1 = bottomLeft[i][0], y1 = bottomLeft[i][1];
            int x2 = topRight[i][0], y2 = topRight[i][1];
            for (int j = i + 1; j < n; j++) {
                int x3 = bottomLeft[j][0], y3 = bottomLeft[j][1];
                int x4 = topRight[j][0], y4 = topRight[j][1];
                int ww = Math.min(x2, x4) - Math.max(x1, x3);
                int h = Math.min(y2, y4) - Math.max(y1, y3);
                int e = Math.min(ww, h);
                if (e > 0) ans = Math.max(ans, (long)e * e);
            }
        }
        return ans;
    }
}
