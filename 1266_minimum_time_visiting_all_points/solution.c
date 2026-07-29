// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

#include <stdlib.h>

static int abs_int(int x) { return x < 0 ? -x : x; }

int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int ans = 0;
    for (int i = 1; i < pointsSize; i++) {
        int dx = abs_int(points[i][0] - points[i - 1][0]);
        int dy = abs_int(points[i][1] - points[i - 1][1]);
        ans += dx > dy ? dx : dy;
    }
    return ans;
}
