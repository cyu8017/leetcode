// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSmaller(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)calloc((size_t)numsSize, sizeof(int));
    int* sortedNums = (int*)malloc((size_t)numsSize * sizeof(int));
    int sortedSize = 0;
    *returnSize = numsSize;

    for (int index = numsSize - 1; index >= 0; index--) {
        int num = nums[index];
        int left = 0;
        int right = sortedSize;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (sortedNums[mid] < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        result[index] = left;
        for (int shift = sortedSize; shift > left; shift--) {
            sortedNums[shift] = sortedNums[shift - 1];
        }
        sortedNums[left] = num;
        sortedSize += 1;
    }

    free(sortedNums);
    return result;
}
