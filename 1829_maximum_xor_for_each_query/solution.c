// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getMaximumXor(int* nums, int numsSize, int maximumBit, int* returnSize) {
    int limit = (1 << maximumBit) - 1;
    int current = 0;
    for (int i = 0; i < numsSize; i++) current ^= nums[i];

    int* result = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = numsSize - 1; i >= 0; i--) {
        result[numsSize - 1 - i] = current ^ limit;
        current ^= nums[i];
    }
    *returnSize = numsSize;
    return result;
}
