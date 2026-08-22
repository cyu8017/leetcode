// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

#include <stdbool.h>

static bool check(int* nums, int n, int target, int k) {
    int cnt = 0, sign = 1;
    for (int i = 0; i < n - 1; i++) {
        int x = nums[i] * sign;
        if (x == target) sign = 1;
        else { sign = -1; cnt++; }
    }
    return cnt <= k && nums[n - 1] * sign == target;
}

bool canMakeEqual(int* nums, int numsSize, int k) {
    return check(nums, numsSize, nums[0], k) || check(nums, numsSize, -nums[0], k);
}
