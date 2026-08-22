// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

#include <stdlib.h>

static int cmp2974(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberGame(int* nums, int numsSize, int* returnSize) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) arr[i] = nums[i];
    qsort(arr, (size_t)numsSize, sizeof(int), cmp2974);
    for (int i = 0; i + 1 < numsSize; i += 2) {
        int t = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = t;
    }
    *returnSize = numsSize;
    return arr;
}
