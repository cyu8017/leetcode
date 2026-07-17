// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

#include <stdlib.h>
#include <string.h>

static int compare_desc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int largestSubmatrix(int** matrix, int matrixSize, int* matrixColSize) {
    int m = matrixSize;
    int n = matrixColSize[0];
    int* heights = (int*)calloc(n, sizeof(int));
    int* sorted = (int*)malloc(n * sizeof(int));
    int best = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            heights[c] = matrix[r][c] ? heights[c] + 1 : 0;
        }
        memcpy(sorted, heights, n * sizeof(int));
        qsort(sorted, n, sizeof(int), compare_desc);
        for (int width = 1; width <= n; width++) {
            int area = width * sorted[width - 1];
            if (area > best) {
                best = area;
            }
        }
    }
    free(heights);
    free(sorted);
    return best;
}
