// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

#include <stdlib.h>

int numSpecial(int** mat, int matSize, int* matColSize) {
    int cols = matColSize[0];
    int* rows = (int*)calloc((size_t)matSize, sizeof(int));
    int* colSum = (int*)calloc((size_t)cols, sizeof(int));
    for (int i = 0; i < matSize; i++) {
        for (int j = 0; j < cols; j++) {
            rows[i] += mat[i][j];
            colSum[j] += mat[i][j];
        }
    }
    int ans = 0;
    for (int i = 0; i < matSize; i++) {
        for (int j = 0; j < cols; j++) {
            if (mat[i][j] == 1 && rows[i] == 1 && colSum[j] == 1) ans++;
        }
    }
    free(rows);
    free(colSum);
    return ans;
}
