// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minDayskVariants(int** points, int pointsSize, int* pointsColSize, int k) {
    (void)pointsColSize;
    int ans = 1000000000;
    int* dists = (int*)malloc((size_t)pointsSize * sizeof(int));
    for (int x = 1; x <= 100; x++) {
        for (int y = 1; y <= 100; y++) {
            for (int i = 0; i < pointsSize; i++) {
                int dx = points[i][0] - x; if (dx < 0) dx = -dx;
                int dy = points[i][1] - y; if (dy < 0) dy = -dy;
                dists[i] = dx + dy;
            }
            qsort(dists, (size_t)pointsSize, sizeof(int), cmpInt);
            if (dists[k - 1] < ans) ans = dists[k - 1];
        }
    }
    free(dists);
    return ans;
}
