// LeetCode 0324 - Wiggle Sort II
// https://leetcode.com/problems/wiggle-sort-ii/

#include <stdlib.h>

static int compareInts(const void* left, const void* right) {
    return (*(const int*)left) - (*(const int*)right);
}

void wiggleSort(int* nums, int numsSize) {
    int* sortedNums = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int index = 0; index < numsSize; index++) {
        sortedNums[index] = nums[index];
    }
    qsort(sortedNums, (size_t)numsSize, sizeof(int), compareInts);
    int left = (numsSize - 1) / 2;
    int right = numsSize - 1;
    for (int index = 0; index < numsSize; index++) {
        if (index % 2 == 0) {
            nums[index] = sortedNums[left--];
        } else {
            nums[index] = sortedNums[right--];
        }
    }
    free(sortedNums);
}
