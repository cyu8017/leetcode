// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

#include <stdlib.h>

static void sort3(int* a) {
    if (a[0] > a[1]) { int t = a[0]; a[0] = a[1]; a[1] = t; }
    if (a[1] > a[2]) { int t = a[1]; a[1] = a[2]; a[2] = t; }
    if (a[0] > a[1]) { int t = a[0]; a[0] = a[1]; a[1] = t; }
}

static int cmpCub(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    if (x[0] != y[0]) return x[0] - y[0];
    if (x[1] != y[1]) return x[1] - y[1];
    return x[2] - y[2];
}

int maxHeight(int** cuboids, int cuboidsSize, int* cuboidsColSize) {
    (void)cuboidsColSize;
    for (int i = 0; i < cuboidsSize; i++) sort3(cuboids[i]);
    qsort(cuboids, (size_t)cuboidsSize, sizeof(int*), cmpCub);
    int* dp = (int*)malloc((size_t)cuboidsSize * sizeof(int));
    int best = 0;
    for (int i = 0; i < cuboidsSize; i++) {
        dp[i] = cuboids[i][2];
        for (int j = 0; j < i; j++) {
            if (cuboids[j][0] <= cuboids[i][0] && cuboids[j][1] <= cuboids[i][1] && cuboids[j][2] <= cuboids[i][2]) {
                int v = dp[j] + cuboids[i][2];
                if (v > dp[i]) dp[i] = v;
            }
        }
        if (dp[i] > best) best = dp[i];
    }
    free(dp);
    return best;
}
