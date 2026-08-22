// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

#include <stdbool.h>

static bool hasPoint(int** points, int n, int x, int y) {
    for (int i = 0; i < n; i++) if (points[i][0] == x && points[i][1] == y) return true;
    return false;
}

int maxRectangleArea(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int ans = -1, n = pointsSize;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
        int x1 = points[i][0], y1 = points[i][1], x2 = points[j][0], y2 = points[j][1];
        if (x1 == x2 || y1 == y2) continue;
        if (!hasPoint(points, n, x1, y2) || !hasPoint(points, n, x2, y1)) continue;
        int minX = x1 < x2 ? x1 : x2, maxX = x1 > x2 ? x1 : x2;
        int minY = y1 < y2 ? y1 : y2, maxY = y1 > y2 ? y1 : y2;
        int ok = 1;
        for (int p = 0; p < n; p++) {
            int x = points[p][0], y = points[p][1];
            if (x > minX && x < maxX && y > minY && y < maxY) { ok = 0; break; }
            int onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) || ((y == minY || y == maxY) && x >= minX && x <= maxX);
            if (onBorder) {
                int isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                if (!isCorner) { ok = 0; break; }
            }
        }
        if (ok) {
            int area = (maxX - minX) * (maxY - minY);
            if (area > ans) ans = area;
        }
    }
    return ans;
}
