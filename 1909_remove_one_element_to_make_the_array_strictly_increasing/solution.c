// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

#include <stdbool.h>

static bool check(int* nums, int n, int skip) {
    int prev = -1;
    int hasPrev = 0;
    for (int i = 0; i < n; i++) {
        if (i == skip) continue;
        if (hasPrev && nums[i] <= prev) return false;
        prev = nums[i];
        hasPrev = 1;
    }
    return true;
}

bool canBeIncreasing(int* nums, int numsSize) {
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] <= nums[i - 1]) {
            return check(nums, numsSize, i - 1) || check(nums, numsSize, i);
        }
    }
    return true;
}
