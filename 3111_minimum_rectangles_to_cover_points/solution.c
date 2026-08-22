// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

#include <stdlib.h>

static int cmp_pts(const void* a, const void* b) {
    int* const* pa = (int* const*)a;
    int* const* pb = (int* const*)b;
    return (*pa)[0] - (*pb)[0];
}

int minRectanglesToCoverPoints(int** points, int pointsSize, int* pointsColSize, int w) {
    (void)pointsColSize;
    qsort(points, (size_t)pointsSize, sizeof(int*), cmp_pts);
    int ans = 0, x1 = -1;
    for (int i = 0; i < pointsSize; i++) {
        int x = points[i][0];
        if (x > x1) {
            ans++;
            x1 = x + w;
        }
    }
    return ans;
}
