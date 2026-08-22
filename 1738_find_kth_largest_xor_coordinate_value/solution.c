// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

#include <stdlib.h>

static int descCompare(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    return (y > x) - (y < x);
}

int kthLargestValue(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int rows = matrixSize;
    int cols = matrixColSize[0];
    int* prev = (int*)calloc(cols + 1, sizeof(int));
    int* cur = (int*)calloc(cols + 1, sizeof(int));
    int* values = (int*)malloc(rows * cols * sizeof(int));
    int index = 0;
    for (int r = 1; r <= rows; r++) {
        for (int c = 1; c <= cols; c++) {
            cur[c] = prev[c] ^ cur[c - 1] ^ prev[c - 1] ^ matrix[r - 1][c - 1];
            values[index++] = cur[c];
        }
        int* tmp = prev;
        prev = cur;
        cur = tmp;
        cur[0] = 0;
    }
    qsort(values, rows * cols, sizeof(int), descCompare);
    int ans = values[k - 1];
    free(prev);
    free(cur);
    free(values);
    return ans;
}
