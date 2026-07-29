// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

#include <stdbool.h>
#include <stdlib.h>

static bool possible(int** prefix, int m, int n, int size, int threshold) {
    for (int r = size; r <= m; r++) {
        for (int c = size; c <= n; c++) {
            int sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size];
            if (sum <= threshold) return true;
        }
    }
    return false;
}

int maxSideLength(int** mat, int matSize, int* matColSize, int threshold) {
    int m = matSize, n = matColSize[0];
    int** prefix = (int**)malloc((size_t)(m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) prefix[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
        }
    }
    int lo = 0, hi = m < n ? m : n;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (possible(prefix, m, n, mid, threshold)) lo = mid;
        else hi = mid - 1;
    }
    for (int i = 0; i <= m; i++) free(prefix[i]);
    free(prefix);
    return lo;
}
