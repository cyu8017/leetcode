// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

#include <stdlib.h>
#include <limits.h>

static long long maxll(long long a, long long b) { return a > b ? a : b; }

long long maxSubarraySum(int* nums, int numsSize, int k) {
    long long inf = LLONG_MIN / 4;
    long long (*f)[4] = calloc((size_t)(numsSize + 1), sizeof(long long[4]));
    for (int i = 0; i <= numsSize; i++) {
        for (int j = 0; j < 4; j++) f[i][j] = inf;
    }
    f[0][0] = 0;
    long long ans = inf;
    for (int i = 1; i <= numsSize; i++) {
        long long x = nums[i - 1];
        f[i][0] = maxll(f[i - 1][0], 0) + x;
        f[i][1] = maxll(maxll(f[i - 1][0], f[i - 1][1]), 0) + x * k;
        f[i][2] = maxll(maxll(f[i - 1][0], f[i - 1][2]), 0) + x / k;
        f[i][3] = maxll(maxll(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x;
        ans = maxll(ans, maxll(maxll(f[i][0], f[i][1]), maxll(f[i][2], f[i][3])));
    }
    free(f);
    return ans;
}
