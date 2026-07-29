// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

#include <stdbool.h>

bool isMajorityElement(int* nums, int numsSize, int target) {
    int lo = 0, hi = numsSize;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] < target) lo = mid + 1; else hi = mid;
    }
    int left = lo;
    lo = 0; hi = numsSize;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] <= target) lo = mid + 1; else hi = mid;
    }
    return lo - left > numsSize / 2;
}
