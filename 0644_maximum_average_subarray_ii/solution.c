// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

#include <stdbool.h>

static bool canReach(int* nums, int n, int k, double mid) {
    double prefix = 0.0;
    for (int i = 0; i < k; i++) prefix += nums[i] - mid;
    if (prefix >= 0) return true;
    double prev = 0.0, minPrev = 0.0;
    for (int i = k; i < n; i++) {
        prefix += nums[i] - mid;
        prev += nums[i - k] - mid;
        if (prev < minPrev) minPrev = prev;
        if (prefix - minPrev >= 0) return true;
    }
    return false;
}

double findMaxAverage(int* nums, int numsSize, int k) {
    double left = nums[0], right = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < left) left = nums[i];
        if (nums[i] > right) right = nums[i];
    }
    for (int iter = 0; iter < 80; iter++) {
        double mid = (left + right) / 2.0;
        if (canReach(nums, numsSize, k, mid)) left = mid;
        else right = mid;
    }
    return left;
}
