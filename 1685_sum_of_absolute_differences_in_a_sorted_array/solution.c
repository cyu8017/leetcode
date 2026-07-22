// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

#include <stdlib.h>

int* getSumAbsoluteDifferences(int* nums, int numsSize, int* returnSize) {
    long long total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    *returnSize = numsSize;
    long long left = 0;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        ans[i] = (int)(x * i - left + (total - left - x) - x * (numsSize - i - 1));
        left += x;
    }
    return ans;
}
