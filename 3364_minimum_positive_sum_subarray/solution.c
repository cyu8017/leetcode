// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

#include <stdlib.h>

int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int n = numsSize;
    int* pref = (int*)malloc((n + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    int ans = 2000000000, found = 0;
    for (int i = 0; i < n; i++) {
        for (int length = l; length <= r && i + length <= n; length++) {
            int s = pref[i + length] - pref[i];
            if (s > 0 && s < ans) { ans = s; found = 1; }
        }
    }
    free(pref);
    return found ? ans : -1;
}
