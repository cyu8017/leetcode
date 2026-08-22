// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

#include <stdlib.h>
#include <stdbool.h>

static bool hasPoint(int* xs, int* ys, int n, int x, int y) {
    for (int i = 0; i < n; i++) if (xs[i] == x && ys[i] == y) return true;
    return false;
}

long long maxRectangleArea(int* xCoord, int xCoordSize, int* yCoord, int yCoordSize) {
    (void)yCoordSize;
    int n = xCoordSize;
    long long ans = -1;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
        int x1 = xCoord[i], y1 = yCoord[i], x2 = xCoord[j], y2 = yCoord[j];
        if (x1 == x2 || y1 == y2) continue;
        if (!hasPoint(xCoord, yCoord, n, x1, y2) || !hasPoint(xCoord, yCoord, n, x2, y1)) continue;
        int minX = x1 < x2 ? x1 : x2, maxX = x1 > x2 ? x1 : x2;
        int minY = y1 < y2 ? y1 : y2, maxY = y1 > y2 ? y1 : y2;
        int ok = 1;
        for (int p = 0; p < n; p++) {
            int x = xCoord[p], y = yCoord[p];
            if (x > minX && x < maxX && y > minY && y < maxY) { ok = 0; break; }
            int onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) || ((y == minY || y == maxY) && x >= minX && x <= maxX);
            if (onBorder) {
                int isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                if (!isCorner) { ok = 0; break; }
            }
        }
        if (ok) {
            long long area = (long long)(maxX - minX) * (maxY - minY);
            if (area > ans) ans = area;
        }
    }
    return ans;
}
