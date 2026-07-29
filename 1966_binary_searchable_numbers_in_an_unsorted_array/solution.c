// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

#include <stdlib.h>
#include <limits.h>

int binarySearchableNumbers(int* nums, int numsSize) {
    int* rightMin = (int*)malloc((size_t)numsSize * sizeof(int));
    rightMin[numsSize - 1] = INT_MAX;
    for (int i = numsSize - 2; i >= 0; i--) {
        rightMin[i] = nums[i + 1] < rightMin[i + 1] ? nums[i + 1] : rightMin[i + 1];
    }
    int leftMax = INT_MIN, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= leftMax && nums[i] <= rightMin[i]) ans++;
        if (nums[i] > leftMax) leftMax = nums[i];
    }
    free(rightMin);
    return ans;
}
