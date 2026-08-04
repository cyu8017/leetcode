// LeetCode 1453 - Maximum Number Of Darts Inside Of A Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

class Solution {
    public int numPoints(int[][] darts, int r) {
        int ans = darts.length > 0 ? 1 : 0;
        for (int i = 0; i < darts.length; i++) {
            for (int j = i + 1; j < darts.length; j++) {
                double x1 = darts[i][0], y1 = darts[i][1], x2 = darts[j][0], y2 = darts[j][1];
                double dx = x2 - x1, dy = y2 - y1, d2 = dx * dx + dy * dy;
                if (d2 > 4.0 * r * r || d2 == 0) continue;
                double d = Math.Sqrt(d2), h = Math.Sqrt(r * r - d2 / 4);
                double mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
                for (int sign : new int[]{ -1, 1 }) {
                    double cx = mx + sign * (-dy) * h / d, cy = my + sign * dx * h / d;
                    int count = 0;
                    for (var p : darts)
                        if ((p[0] - cx) * (p[0] - cx) + (p[1] - cy) * (p[1] - cy) <= r * r + 1e-7) count++;
                    ans = Math.max(ans, count);
                }
            }
        }
        return ans;
    }
}
