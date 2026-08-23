// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

import java.util.*;

class Solution {
    public double minAreaFreeRect(int[][] points) {
        int n = points.length;
        Map<String, List<int[]>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long cx = points[i][0] + points[j][0];
                long cy = points[i][1] + points[j][1];
                long dx = points[i][0] - points[j][0];
                long dy = points[i][1] - points[j][1];
                long dist = dx * dx + dy * dy;
                String key = cx + "#" + cy + "#" + dist;
                groups.computeIfAbsent(key, k -> new ArrayList<>()).add(new int[] {i, j});
            }
        }
        double ans = 1e300;
        for (List<int[]> pairs : groups.values()) {
            for (int a = 0; a < pairs.size(); a++) {
                for (int b = a + 1; b < pairs.size(); b++) {
                    int p1 = pairs.get(a)[0], p2 = pairs.get(b)[0], q2 = pairs.get(b)[1];
                    double d1 = Math.hypot(points[p1][0] - points[p2][0], points[p1][1] - points[p2][1]);
                    double d2 = Math.hypot(points[p1][0] - points[q2][0], points[p1][1] - points[q2][1]);
                    double area = d1 * d2;
                    if (area > 0) ans = Math.min(ans, area);
                }
            }
        }
        return ans >= 1e299 ? 0.0 : ans;
    }
}
