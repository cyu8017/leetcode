// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

#include <limits.h>

static long long llmax(long long a, long long b) { return a > b ? a : b; }
static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

long long maximumProduct(int* nums, int numsSize, int m) {
    long long ans = LLONG_MIN;
    int mx = INT_MIN, mi = INT_MAX;
    for (int i = m - 1; i < numsSize; i++) {
        int x = nums[i], y = nums[i - m + 1];
        mi = imin(mi, y); mx = imax(mx, y);
        ans = llmax(ans, llmax((long long)x * mi, (long long)x * mx));
    }
    return ans;
}
