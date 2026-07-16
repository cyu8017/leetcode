// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#include <stdlib.h>

static int lower_bound(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize;

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

static int upper_bound(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize;

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));

    if (numsSize == 0) {
        result[0] = -1;
        result[1] = -1;
        return result;
    }

    int start = lower_bound(nums, numsSize, target);
    if (start == numsSize || nums[start] != target) {
        result[0] = -1;
        result[1] = -1;
        return result;
    }

    result[0] = start;
    result[1] = upper_bound(nums, numsSize, target) - 1;
    return result;
}
