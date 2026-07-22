// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxWidthOfVerticalArea(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int* xs = (int*)malloc((size_t)pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; i++) xs[i] = points[i][0];
    qsort(xs, (size_t)pointsSize, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 1; i < pointsSize; i++) {
        int d = xs[i] - xs[i - 1];
        if (d > ans) ans = d;
    }
    free(xs);
    return ans;
}
