// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

#include <stdlib.h>

static int cmp_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

#define INF3505 (1LL << 62)

long long minOperations(int* nums, int numsSize, int x, int k) {
    int n = numsSize;
    long long* minOps = (long long*)malloc((size_t)(n - x + 1) * sizeof(long long));
    for (int i = 0; i + x <= n; i++) {
        int* w = (int*)malloc((size_t)x * sizeof(int));
        for (int j = 0; j < x; j++) w[j] = nums[i + j];
        qsort(w, (size_t)x, sizeof(int), cmp_asc);
        int med = w[(x - 1) / 2];
        long long ops = 0;
        for (int j = 0; j < x; j++) {
            long long d = w[j] - med;
            if (d < 0) d = -d;
            ops += d;
        }
        minOps[i] = ops;
        free(w);
    }
    long long** dp = (long long**)malloc((size_t)(n + 1) * sizeof(long long*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (long long*)malloc((size_t)(k + 1) * sizeof(long long));
        for (int j = 0; j <= k; j++) dp[i][j] = INF3505;
    }
    dp[n][0] = 0;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j <= k; j++) {
            dp[i][j] = dp[i + 1][j];
            if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j])
                dp[i][j] = minOps[i] + dp[i + x][j - 1];
        }
    }
    long long ans = dp[0][k];
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(dp); free(minOps);
    return ans;
}
