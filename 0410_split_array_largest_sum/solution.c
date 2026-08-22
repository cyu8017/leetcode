// LeetCode 0410 - Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

#include <stdbool.h>

static bool can_split(int* nums, int numsSize, int k, int limit) {
    int parts = 1;
    int current = 0;

    for (int index = 0; index < numsSize; index++) {
        if (current + nums[index] > limit) {
            parts += 1;
            current = 0;
        }
        current += nums[index];
    }

    return parts <= k;
}

int splitArray(int* nums, int numsSize, int k) {
    int left = nums[0];
    int right = 0;

    for (int index = 0; index < numsSize; index++) {
        if (nums[index] > left) {
            left = nums[index];
        }
        right += nums[index];
    }

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (can_split(nums, numsSize, k, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
