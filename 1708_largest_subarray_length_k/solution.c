// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* largestSubarray(int* nums, int numsSize, int k, int* returnSize) {
    int start = 0;
    for (int i = 1; i + k <= numsSize; i++) {
        if (nums[i] > nums[start]) {
            start = i;
        }
    }
    int* result = (int*)malloc(k * sizeof(int));
    for (int i = 0; i < k; i++) {
        result[i] = nums[start + i];
    }
    *returnSize = k;
    return result;
}
