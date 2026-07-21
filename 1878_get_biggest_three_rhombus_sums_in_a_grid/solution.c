// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

static void addUnique(int* values, int* size, int value) {
    for (int i = 0; i < *size; i++) {
        if (values[i] == value) return;
    }
    values[(*size)++] = value;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getBiggestThree(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int* s1 = (int*)calloc((size_t)(m + 1) * (n + 2), sizeof(int));
    int* s2 = (int*)calloc((size_t)(m + 1) * (n + 2), sizeof(int));
    #define S1(i, j) s1[(i) * (n + 2) + (j)]
    #define S2(i, j) s2[(i) * (n + 2) + (j)]

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int value = grid[i - 1][j - 1];
            S1(i, j) = S1(i - 1, j - 1) + value;
            S2(i, j) = S2(i - 1, j + 1) + value;
        }
    }

    int cap = m * n * 20;
    if (cap < 16) cap = 16;
    int* values = (int*)malloc((size_t)cap * sizeof(int));
    int size = 0;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int value = grid[i - 1][j - 1];
            int limit = i - 1;
            if (m - i < limit) limit = m - i;
            if (j - 1 < limit) limit = j - 1;
            if (n - j < limit) limit = n - j;
            addUnique(values, &size, value);
            for (int k = 1; k <= limit; k++) {
                int a = S1(i + k, j) - S1(i, j - k);
                int b = S1(i, j + k) - S1(i - k, j);
                int c = S2(i, j - k) - S2(i - k, j);
                int d = S2(i + k, j) - S2(i, j + k);
                int sum = a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1];
                addUnique(values, &size, sum);
            }
        }
    }

    qsort(values, (size_t)size, sizeof(int), cmpDesc);
    int out = size < 3 ? size : 3;
    int* result = (int*)malloc((size_t)out * sizeof(int));
    for (int i = 0; i < out; i++) result[i] = values[i];
    free(s1);
    free(s2);
    free(values);
    *returnSize = out;
    return result;
    #undef S1
    #undef S2
}
