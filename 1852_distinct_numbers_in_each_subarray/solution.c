// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distinctNumbers(int* nums, int numsSize, int k, int* returnSize) {
    int outLen = numsSize - k + 1;
    int* result = (int*)malloc((size_t)outLen * sizeof(int));
    int* counts = (int*)calloc(100001, sizeof(int));
    int distinct = 0;
    for (int i = 0; i < k; i++) {
        if (counts[nums[i]]++ == 0) distinct++;
    }
    result[0] = distinct;
    int left = 0;
    int idx = 1;
    for (int right = k; right < numsSize; right++) {
        if (counts[nums[right]]++ == 0) distinct++;
        if (--counts[nums[left]] == 0) distinct--;
        left++;
        result[idx++] = distinct;
    }
    free(counts);
    *returnSize = outLen;
    return result;
}
