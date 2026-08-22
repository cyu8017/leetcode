// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

#include <stdlib.h>
#include <string.h>

int* applyOperations(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i + 1 < numsSize; i++) {
        if (nums[i] == nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }
    int* ans = (int*)calloc((size_t)numsSize, sizeof(int));
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != 0) ans[j++] = nums[i];
    }
    *returnSize = numsSize;
    return ans;
}
