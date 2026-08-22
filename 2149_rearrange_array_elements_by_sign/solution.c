// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

#include <stdlib.h>

int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int pos = 0, neg = 1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > 0) { ans[pos] = nums[i]; pos += 2; }
        else { ans[neg] = nums[i]; neg += 2; }
    }
    *returnSize = numsSize;
    return ans;
}
