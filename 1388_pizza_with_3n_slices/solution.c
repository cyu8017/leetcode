// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

#include <stdlib.h>

static int line(int* a, int n, int k) {
    int rows = n + 2;
    int* dp = (int*)calloc(rows * (k + 1), sizeof(int));
    for (int i = 0; i < n; i++) {
        int ii = i + 2;
        for (int j = 1; j <= k; j++) {
            int skip = dp[(ii - 1) * (k + 1) + j];
            int take = dp[(ii - 2) * (k + 1) + (j - 1)] + a[i];
            dp[ii * (k + 1) + j] = skip > take ? skip : take;
        }
    }
    int ans = dp[(n + 1) * (k + 1) + k];
    free(dp);
    return ans;
}

int maxSizeSlices(int* slices, int slicesSize) {
    int k = slicesSize / 3;
    int* a1 = (int*)malloc((slicesSize - 1) * sizeof(int));
    int* a2 = (int*)malloc((slicesSize - 1) * sizeof(int));
    for (int i = 0; i < slicesSize - 1; i++) a1[i] = slices[i];
    for (int i = 1; i < slicesSize; i++) a2[i - 1] = slices[i];
    int ans1 = line(a1, slicesSize - 1, k);
    int ans2 = line(a2, slicesSize - 1, k);
    free(a1); free(a2);
    return ans1 > ans2 ? ans1 : ans2;
}
