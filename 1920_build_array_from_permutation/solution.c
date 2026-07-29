// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

#include <stdlib.h>

int* buildArray(int* nums, int numsSize, int* returnSize) {
    int* res = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) res[i] = nums[nums[i]];
    *returnSize = numsSize;
    return res;
}
