// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minMoves2(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int median = nums[numsSize / 2];
    int total = 0;
    for (int i = 0; i < numsSize; i++) {
        int diff = nums[i] - median;
        total += diff < 0 ? -diff : diff;
    }
    return total;
}
