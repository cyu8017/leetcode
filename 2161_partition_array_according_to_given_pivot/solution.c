// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

#include <stdlib.h>

int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int p = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] < pivot) ans[p++] = nums[i];
    for (int i = 0; i < numsSize; i++) if (nums[i] == pivot) ans[p++] = nums[i];
    for (int i = 0; i < numsSize; i++) if (nums[i] > pivot) ans[p++] = nums[i];
    *returnSize = numsSize;
    return ans;
}
