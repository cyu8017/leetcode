// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

#include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* result = malloc((size_t)numsSize * sizeof(int));
    int prefix = 1;
    for (int index = 0; index < numsSize; index++) {
        result[index] = prefix;
        prefix *= nums[index];
    }
    int suffix = 1;
    for (int index = numsSize - 1; index >= 0; index--) {
        result[index] *= suffix;
        suffix *= nums[index];
    }
    *returnSize = numsSize;
    return result;
}
