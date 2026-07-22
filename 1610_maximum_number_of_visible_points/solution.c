// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

#include <stdlib.h>
#include <math.h>

static int cmpDouble(const void* a, const void* b) {
    double x = *(const double*)a, y = *(const double*)b;
    return (x > y) - (x < y);
}

int visiblePoints(int** points, int pointsSize, int* pointsColSize, int angle, int* location, int locationSize) {
    (void)pointsColSize; (void)locationSize;
    double* a = (double*)malloc((size_t)pointsSize * sizeof(double));
    int n = 0, same = 0;
    for (int i = 0; i < pointsSize; i++) {
        double dx = points[i][0] - location[0];
        double dy = points[i][1] - location[1];
        if (dx == 0 && dy == 0) same++;
        else a[n++] = atan2(dy, dx);
    }
    qsort(a, (size_t)n, sizeof(double), cmpDouble);
    double* ext = (double*)malloc((size_t)(2 * n) * sizeof(double));
    for (int i = 0; i < n; i++) {
        ext[i] = a[i];
        ext[i + n] = a[i] + 2.0 * acos(-1.0);
    }
    double width = angle * acos(-1.0) / 180.0 + 1e-12;
    int left = 0, best = 0;
    for (int right = 0; right < 2 * n; right++) {
        while (ext[right] - ext[left] > width) left++;
        int cur = right - left + 1;
        if (cur > n) cur = n;
        if (cur > best) best = cur;
    }
    free(a); free(ext);
    return best + same;
}
