// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int lower_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int* countRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize, int** points, int pointsSize, int* pointsColSize, int* returnSize) {
    (void)rectanglesColSize; (void)pointsColSize;
    int* byH[101];
    int sz[101] = {0}, cap[101] = {0};
    for (int i = 0; i < 101; i++) byH[i] = NULL;
    for (int i = 0; i < rectanglesSize; i++) {
        int h = rectangles[i][1], x = rectangles[i][0];
        if (sz[h] == cap[h]) {
            cap[h] = cap[h] ? cap[h] * 2 : 4;
            byH[h] = (int*)realloc(byH[h], (size_t)cap[h] * sizeof(int));
        }
        byH[h][sz[h]++] = x;
    }
    for (int h = 1; h <= 100; h++) {
        if (sz[h]) qsort(byH[h], (size_t)sz[h], sizeof(int), cmp_int);
    }
    int* ans = (int*)malloc((size_t)pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; i++) {
        int x = points[i][0], y = points[i][1], cnt = 0;
        for (int h = y; h <= 100; h++) {
            if (!sz[h]) continue;
            int j = lower_bound(byH[h], sz[h], x);
            cnt += sz[h] - j;
        }
        ans[i] = cnt;
    }
    for (int i = 0; i < 101; i++) free(byH[i]);
    *returnSize = pointsSize;
    return ans;
}
