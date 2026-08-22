// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

#include <limits.h>

static int min3942(int a, int b) { return a < b ? a : b; }

static int check3942(int* nums, int n, int zero, int step) {
    for (int i = 1; i < n; i++) {
        int prev = (zero + (i - 1) * step % n + n) % n;
        int curr = (zero + i * step % n + n) % n;
        /* careful with negative step */
        prev = ((zero + (i - 1) * step) % n + n) % n;
        curr = ((zero + i * step) % n + n) % n;
        if (nums[prev] > nums[curr]) return 0;
    }
    return 1;
}

int minOperations(int* nums, int numsSize) {
    int n = numsSize, zero = 0;
    for (int i = 0; i < n; i++) if (nums[i] == 0) { zero = i; break; }
    int ans = INT_MAX;
    if (check3942(nums, n, zero, 1)) {
        ans = min3942(ans, zero);
        ans = min3942(ans, n - zero + 2);
    }
    if (check3942(nums, n, zero, -1)) {
        ans = min3942(ans, zero + 2);
        ans = min3942(ans, n - zero);
    }
    return ans == INT_MAX ? -1 : ans;
}
