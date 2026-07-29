// LeetCode 1389 - Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

#include <stdlib.h>

int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize) {
    (void)indexSize;
    int* out = (int*)malloc(numsSize * sizeof(int));
    int size = 0;
    for (int t = 0; t < numsSize; t++) {
        int i = index[t], x = nums[t];
        for (int j = size; j > i; j--) out[j] = out[j - 1];
        out[i] = x;
        size++;
    }
    *returnSize = numsSize;
    return out;
}
