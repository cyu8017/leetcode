// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* leftRightDifference(int* nums, int numsSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int left = 0;
    for (int i = 0; i < numsSize; i++) {
        int right = total - left - nums[i];
        int d = left - right;
        if (d < 0) d = -d;
        ans[i] = d;
        left += nums[i];
    }
    *returnSize = numsSize;
    return ans;
}
