// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int arrayPairSum(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int total = 0;
    for (int i = 0; i < numsSize; i += 2) {
        total += nums[i];
    }
    return total;
}
