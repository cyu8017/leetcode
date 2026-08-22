// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static long long llmax(long long a, long long b) { return a > b ? a : b; }

long long maximumStrength(int* nums, int numsSize, int k) {
    int n = numsSize;
    const long long INF = LLONG_MIN / 2;
    long long*** f = (long long***)malloc((size_t)(n + 1) * sizeof(long long**));
    for (int i = 0; i <= n; i++) {
        f[i] = (long long**)malloc((size_t)(k + 1) * sizeof(long long*));
        for (int j = 0; j <= k; j++) {
            f[i][j] = (long long*)malloc(2 * sizeof(long long));
            f[i][j][0] = f[i][j][1] = INF;
        }
    }
    f[0][0][0] = 0;
    for (int i = 1; i <= n; i++) {
        long long x = nums[i - 1];
        for (int j = 0; j <= k; j++) {
            long long sign = (j & 1) ? 1 : -1;
            long long val = sign * x * (k - j + 1);
            f[i][j][0] = llmax(f[i - 1][j][0], f[i - 1][j][1]);
            f[i][j][1] = llmax(f[i][j][1], f[i - 1][j][1] + val);
            if (j > 0) {
                long long t = llmax(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + val;
                f[i][j][1] = llmax(f[i][j][1], t);
            }
        }
    }
    long long ans = llmax(f[n][k][0], f[n][k][1]);
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= k; j++) free(f[i][j]);
        free(f[i]);
    }
    free(f);
    return ans;
}
