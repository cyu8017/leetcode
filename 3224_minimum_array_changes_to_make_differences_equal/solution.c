// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

#include <stdlib.h>

static int max3224(int a, int b) { return a > b ? a : b; }

int minChanges(int* nums, int numsSize, int k) {
    int* d = calloc(k + 2, sizeof(int));
    int n = numsSize;
    for (int i = 0; i < n / 2; i++) {
        int x = nums[i], y = nums[n - 1 - i];
        if (x > y) { int t = x; x = y; y = t; }
        d[0] += 1;
        d[y - x] -= 1;
        d[y - x + 1] += 1;
        int m = max3224(y, k - x) + 1;
        d[m] -= 1;
        d[m] += 2;
    }
    int ans = n, s = 0;
    for (int i = 0; i <= k + 1; i++) {
        s += d[i];
        if (s < ans) ans = s;
    }
    free(d);
    return ans;
}
