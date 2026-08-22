// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodSubsetofBinaryMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int n = gridColSize[0];
    int first[1 << 5];
    memset(first, -1, sizeof(first));
    for (int i = 0; i < gridSize; i++) {
        int mask = 0;
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 1) mask |= 1 << j;
        if (mask == 0) {
            int* ans = (int*)malloc(sizeof(int));
            ans[0] = i;
            *returnSize = 1;
            return ans;
        }
        for (int m = 0; m < (1 << n); m++) {
            if (first[m] >= 0 && (m & mask) == 0) {
                int* ans = (int*)malloc(2 * sizeof(int));
                if (first[m] < i) { ans[0] = first[m]; ans[1] = i; }
                else { ans[0] = i; ans[1] = first[m]; }
                *returnSize = 2;
                return ans;
            }
        }
        if (first[mask] < 0) first[mask] = i;
    }
    *returnSize = 0;
    return NULL;
}
