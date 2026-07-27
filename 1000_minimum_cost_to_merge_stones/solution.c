// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

int mergeStones(int* stones, int stonesSize, int k) {
    int n = stonesSize;
    if ((n - 1) % (k - 1) != 0) return -1;
    int* prefix = (int*)malloc((size_t)(n + 1) * sizeof(int));
    prefix[0] = 0;
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];
    int* dp = (int*)calloc((size_t)n * n, sizeof(int));
    for (int length = k; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            int best = INT_MAX;
            for (int m = i; m < j; m += k - 1) {
                int cost = dp[i * n + m] + dp[(m + 1) * n + j];
                if (cost < best) best = cost;
            }
            if ((length - 1) % (k - 1) == 0) best += prefix[j + 1] - prefix[i];
            dp[i * n + j] = best;
        }
    }
    int ans = dp[0 * n + (n - 1)];
    free(prefix);
    free(dp);
    return ans;
}
