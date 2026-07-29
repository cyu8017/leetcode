// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

#include <stdlib.h>

int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {
    (void)indicesColSize;
    int* rows = (int*)calloc((size_t)m, sizeof(int));
    int* cols = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < indicesSize; i++) {
        rows[indices[i][0]] ^= 1;
        cols[indices[i][1]] ^= 1;
    }
    int ans = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if ((rows[r] ^ cols[c]) & 1) ans++;
        }
    }
    free(rows);
    free(cols);
    return ans;
}
