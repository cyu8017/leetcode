// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

#include <stdlib.h>
#include <string.h>

static int* nums3891;
static int n3891;
static long long memo3891[100005][2];
static char seen3891[100005][2];

static long long maxll3891(long long a, long long b) { return a > b ? a : b; }
static int maxi3891(int a, int b) { return a > b ? a : b; }

static long long dfs3891(int i, int j) {
    if (i >= n3891 - 1) return 0;
    if (seen3891[i][j]) return memo3891[i][j];
    int cost = maxi3891(0, maxi3891(nums3891[i - 1], nums3891[i + 1]) + 1 - nums3891[i]);
    long long ans = (long long)cost + dfs3891(i + 2, j);
    if (j > 0) {
        long long t = dfs3891(i + 1, 0);
        if (t < ans) ans = t;
    }
    seen3891[i][j] = 1;
    memo3891[i][j] = ans;
    return ans;
}

long long minIncrease(int* nums, int numsSize) {
    nums3891 = nums;
    n3891 = numsSize;
    memset(seen3891, 0, sizeof(seen3891));
    return dfs3891(1, (n3891 & 1) ^ 1);
}
