// LeetCode 0628 - Maximum Product of Three Numbers
// https://leetcode.com/problems/maximum-product-of-three-numbers/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maximumProduct(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int a = nums[numsSize - 1] * nums[numsSize - 2] * nums[numsSize - 3];
    int b = nums[0] * nums[1] * nums[numsSize - 1];
    return a > b ? a : b;
}
