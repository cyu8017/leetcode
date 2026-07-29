// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

#include <stdlib.h>

int* findDiagonalOrder(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += numsColSize[i];
    int maxDiag = 0;
    for (int r = 0; r < numsSize; r++)
        if (r + numsColSize[r] - 1 > maxDiag) maxDiag = r + numsColSize[r] - 1;
    int* dsize = (int*)calloc(maxDiag + 1, sizeof(int));
    int* dcap = (int*)calloc(maxDiag + 1, sizeof(int));
    int** diags = (int**)calloc(maxDiag + 1, sizeof(int*));
    for (int r = 0; r < numsSize; r++) {
        for (int c = 0; c < numsColSize[r]; c++) {
            int d = r + c;
            if (dsize[d] == dcap[d]) {
                dcap[d] = dcap[d] ? dcap[d] * 2 : 8;
                diags[d] = (int*)realloc(diags[d], dcap[d] * sizeof(int));
            }
            diags[d][dsize[d]++] = nums[r][c];
        }
    }
    int* ans = (int*)malloc(total * sizeof(int));
    int idx = 0;
    for (int d = 0; d <= maxDiag; d++)
        for (int i = dsize[d] - 1; i >= 0; i--) ans[idx++] = diags[d][i];
    for (int d = 0; d <= maxDiag; d++) free(diags[d]);
    free(diags); free(dsize); free(dcap);
    *returnSize = total;
    return ans;
}
