// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

#include <stdlib.h>

static int gCount[201];

static int cmpFreq(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    int cx = gCount[x + 100], cy = gCount[y + 100];
    if (cx != cy) return cx - cy;
    return y - x;
}

int* frequencySort(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i < 201; i++) gCount[i] = 0;
    for (int i = 0; i < numsSize; i++) gCount[nums[i] + 100]++;
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) ans[i] = nums[i];
    qsort(ans, (size_t)numsSize, sizeof(int), cmpFreq);
    *returnSize = numsSize;
    return ans;
}
