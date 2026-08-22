// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rowAndMaximumOnes(int** mat, int matSize, int* matColSize, int* returnSize) {
    int bestRow = 0, bestCnt = -1;
    for (int i = 0; i < matSize; i++) {
        int cnt = 0;
        for (int j = 0; j < matColSize[i]; j++) cnt += mat[i][j];
        if (cnt > bestCnt) {
            bestCnt = cnt;
            bestRow = i;
        }
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = bestRow;
    ans[1] = bestCnt;
    *returnSize = 2;
    return ans;
}
