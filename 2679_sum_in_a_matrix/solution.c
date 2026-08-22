// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

#include <stdlib.h>

static int cmpInt2679(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int matrixSum(int** nums, int numsSize, int* numsColSize) {
    for (int i = 0; i < numsSize; i++)
        qsort(nums[i], (size_t)numsColSize[i], sizeof(int), cmpInt2679);
    int ans = 0, n = numsColSize[0];
    for (int c = 0; c < n; c++) {
        int mx = 0;
        for (int r = 0; r < numsSize; r++)
            if (nums[r][c] > mx) mx = nums[r][c];
        ans += mx;
    }
    return ans;
}
