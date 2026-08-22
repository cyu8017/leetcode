// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

#include <stdlib.h>
#include <string.h>

static int gcd3444(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }
static int lcm3444(int a, int b) { return a / gcd3444(a, b) * b; }

int minimumIncrements(int* nums, int numsSize, int* target, int targetSize) {
    int m = targetSize, N = 1 << m;
    const long long INF = 1000000000000000000LL;
    long long* dp = (long long*)malloc(N * sizeof(long long));
    long long* ndp = (long long*)malloc(N * sizeof(long long));
    for (int i = 0; i < N; i++) dp[i] = INF; dp[0] = 0;
    for (int xi = 0; xi < numsSize; xi++) {
        int x = nums[xi];
        memcpy(ndp, dp, N * sizeof(long long));
        for (int mask = 0; mask < N; mask++) {
            if (dp[mask] >= INF) continue;
            for (int sub = 1; sub < N; sub++) {
                int lcm = 1, ok = 1;
                for (int i = 0; i < m; i++) if (sub & (1 << i)) {
                    lcm = lcm3444(lcm, target[i]);
                    if (lcm > 1000000000) { ok = 0; break; }
                }
                if (!ok) continue;
                int cost = (lcm - x % lcm) % lcm;
                int nmask = mask | sub;
                if (dp[mask] + cost < ndp[nmask]) ndp[nmask] = dp[mask] + cost;
            }
        }
        long long* tmp = dp; dp = ndp; ndp = tmp;
    }
    int ans = (int)dp[N - 1];
    free(dp); free(ndp);
    return ans;
}
