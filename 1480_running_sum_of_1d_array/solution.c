// LeetCode 1480 - Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

#include <stdlib.h>

int* runningSum(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    ans[0] = nums[0];
    for (int i = 1; i < numsSize; i++) ans[i] = ans[i - 1] + nums[i];
    *returnSize = numsSize;
    return ans;
}
