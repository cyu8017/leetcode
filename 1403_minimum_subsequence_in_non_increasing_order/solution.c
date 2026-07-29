// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

int* minSubsequence(int* nums, int numsSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    int* sorted = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) sorted[i] = nums[i];
    qsort(sorted, numsSize, sizeof(int), cmp_desc);
    int* ans = (int*)malloc(numsSize * sizeof(int));
    int chosen = 0, an = 0;
    for (int i = 0; i < numsSize; i++) {
        ans[an++] = sorted[i];
        chosen += sorted[i];
        if (chosen > total - chosen) break;
    }
    free(sorted);
    *returnSize = an;
    return ans;
}
