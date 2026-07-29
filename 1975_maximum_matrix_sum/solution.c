// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

#include <stdlib.h>

long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {
    long long sum = 0;
    int negatives = 0;
    int minAbs = abs(matrix[0][0]);
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixColSize[i]; j++) {
            int v = matrix[i][j];
            int a = abs(v);
            sum += a;
            if (v < 0) negatives++;
            if (a < minAbs) minAbs = a;
        }
    }
    if (negatives % 2) sum -= 2LL * minAbs;
    return sum;
}
