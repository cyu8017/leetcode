// LeetCode 0973 - K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

#include <stdlib.h>

static int* g_pts;
static int cmpDist(const void* a, const void* b) {
    int i = *(const int*)a, j = *(const int*)b;
    long long di = (long long)g_pts[2*i]*g_pts[2*i] + (long long)g_pts[2*i+1]*g_pts[2*i+1];
    long long dj = (long long)g_pts[2*j]*g_pts[2*j] + (long long)g_pts[2*j+1]*g_pts[2*j+1];
    return di < dj ? -1 : di > dj ? 1 : 0;
}

int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int** returnColumnSizes) {
    (void)pointsColSize;
    int* flat = (int*)malloc((size_t)pointsSize * 2 * sizeof(int));
    int* idx = (int*)malloc((size_t)pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; i++) {
        flat[2*i] = points[i][0]; flat[2*i+1] = points[i][1];
        idx[i] = i;
    }
    g_pts = flat;
    qsort(idx, (size_t)pointsSize, sizeof(int), cmpDist);
    int** ans = (int**)malloc((size_t)k * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        ans[i][0] = points[idx[i]][0];
        ans[i][1] = points[idx[i]][1];
        (*returnColumnSizes)[i] = 2;
    }
    free(flat); free(idx);
    *returnSize = k;
    return ans;
}
