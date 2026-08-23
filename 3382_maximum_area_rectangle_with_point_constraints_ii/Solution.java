// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public long maxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.length;
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = xCoord[i];
            points[i][1] = yCoord[i];
        }
        Set<Long> set = new HashSet<>();
        for (int[] p : points) set.add(pack(p[0], p[1]));
        long ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue;
                if (!set.contains(pack(x1, y2)) || !set.contains(pack(x2, y1))) continue;
                int minX = Math.min(x1, x2), maxX = Math.max(x1, x2);
                int minY = Math.min(y1, y2), maxY = Math.max(y1, y2);
                boolean ok = true;
                for (int[] p : points) {
                    int x = p[0], y = p[1];
                    if (x > minX && x < maxX && y > minY && y < maxY) { ok = false; break; }
                    boolean onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                            ((y == minY || y == maxY) && x >= minX && x <= maxX);
                    if (onBorder) {
                        boolean isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                        if (!isCorner) { ok = false; break; }
                    }
                }
                if (ok) {
                    long area = (long) (maxX - minX) * (maxY - minY);
                    if (area > ans) ans = area;
                }
            }
        }
        return ans;
    }

    private static long pack(int x, int y) {
        return ((long) x << 32) ^ (y & 0xffffffffL);
    }
}
