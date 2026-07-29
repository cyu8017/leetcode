// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

#include <stdlib.h>

int* findPeakGrid(int** mat, int matSize, int* matColSize, int* returnSize) {
    int rows = matSize, cols = matColSize[0];
    int lo = 0, hi = cols - 1;
    int* res = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int maxRow = 0;
        for (int r = 1; r < rows; r++) {
            if (mat[r][mid] > mat[maxRow][mid]) maxRow = r;
        }
        int left = mid ? mat[maxRow][mid - 1] : -1;
        int right = mid + 1 < cols ? mat[maxRow][mid + 1] : -1;
        if (mat[maxRow][mid] >= left && mat[maxRow][mid] >= right) {
            res[0] = maxRow;
            res[1] = mid;
            return res;
        }
        if (left > mat[maxRow][mid]) hi = mid - 1;
        else lo = mid + 1;
    }
    res[0] = 0;
    res[1] = 0;
    return res;
}
