// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

#include <stdbool.h>

bool hasIncreasingSubarrays(int* nums, int numsSize, int k) {
    int n = numsSize;
    for (int i = 0; i + 2 * k <= n; i++) {
        int ok1 = 1, ok2 = 1;
        for (int j = i; j + 1 < i + k; j++) if (nums[j] >= nums[j + 1]) { ok1 = 0; break; }
        for (int j = i + k; j + 1 < i + 2 * k; j++) if (nums[j] >= nums[j + 1]) { ok2 = 0; break; }
        if (ok1 && ok2) return true;
    }
    return false;
}
