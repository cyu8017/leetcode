// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

#include <stdbool.h>
#include <stdlib.h>

static int abs_i(int x) { return x < 0 ? -x : x; }

static bool inCircle(int x, int y, int cx, int cy, int r) {
    long long dx = x - cx, dy = y - cy;
    return dx * dx + dy * dy <= (long long)r * r;
}

static bool crossLeftTop(int cx, int cy, int r, int xCorner, int yCorner) {
    bool a = abs_i(cx) <= r && cy >= 0 && cy <= yCorner;
    bool b = abs_i(cy - yCorner) <= r && cx >= 0 && cx <= xCorner;
    return a || b;
}

static bool crossRightBottom(int cx, int cy, int r, int xCorner, int yCorner) {
    bool a = abs_i(cx - xCorner) <= r && cy >= 0 && cy <= yCorner;
    bool b = abs_i(cy) <= r && cx >= 0 && cx <= xCorner;
    return a || b;
}

static bool dfs3235(int i, int** circles, int circlesSize, int* circlesColSize,
                    bool* vis, int xCorner, int yCorner) {
    (void)circlesColSize;
    int x1 = circles[i][0], y1 = circles[i][1], r1 = circles[i][2];
    if (crossRightBottom(x1, y1, r1, xCorner, yCorner)) return true;
    vis[i] = true;
    for (int j = 0; j < circlesSize; j++) {
        if (vis[j]) continue;
        int x2 = circles[j][0], y2 = circles[j][1], r2 = circles[j][2];
        long long d2 = (long long)(x1 - x2) * (x1 - x2) + (long long)(y1 - y2) * (y1 - y2);
        long long rr = (long long)(r1 + r2) * (r1 + r2);
        if (d2 > rr) continue;
        if ((long long)x1 * r2 + (long long)x2 * r1 < (long long)(r1 + r2) * xCorner &&
            (long long)y1 * r2 + (long long)y2 * r1 < (long long)(r1 + r2) * yCorner &&
            dfs3235(j, circles, circlesSize, circlesColSize, vis, xCorner, yCorner)) {
            return true;
        }
    }
    return false;
}

bool canReachCorner(int xCorner, int yCorner, int** circles, int circlesSize, int* circlesColSize) {
    bool* vis = (bool*)calloc((size_t)circlesSize, sizeof(bool));
    for (int i = 0; i < circlesSize; i++) {
        int x = circles[i][0], y = circles[i][1], r = circles[i][2];
        if (inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r)) {
            free(vis);
            return false;
        }
        if (!vis[i] && crossLeftTop(x, y, r, xCorner, yCorner) &&
            dfs3235(i, circles, circlesSize, circlesColSize, vis, xCorner, yCorner)) {
            free(vis);
            return false;
        }
    }
    free(vis);
    return true;
}
