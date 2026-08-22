// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

#include <stdlib.h>

int* findDegrees(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    int* ans = malloc((size_t)matrixSize * sizeof(int));
    for (int i = 0; i < matrixSize; i++) {
        int s = 0;
        for (int j = 0; j < matrixColSize[i]; j++) s += matrix[i][j];
        ans[i] = s;
    }
    *returnSize = matrixSize;
    return ans;
}
