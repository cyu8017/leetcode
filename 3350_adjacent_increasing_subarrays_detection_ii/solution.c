// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

#include <stdlib.h>
#include <stdbool.h>

int maxIncreasingSubarrays(int* nums, int numsSize) {
    int n = numsSize;
    int* up = (int*)malloc(n * sizeof(int));
    up[n - 1] = 1;
    for (int i = n - 2; i >= 0; i--) up[i] = nums[i] < nums[i + 1] ? up[i + 1] + 1 : 1;
    int lo = 1, hi = n / 2;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2, ok = 0;
        for (int i = 0; i + 2 * mid <= n; i++) {
            if (up[i] >= mid && up[i + mid] >= mid) { ok = 1; break; }
        }
        if (ok) lo = mid; else hi = mid - 1;
    }
    free(up);
    return lo;
}
