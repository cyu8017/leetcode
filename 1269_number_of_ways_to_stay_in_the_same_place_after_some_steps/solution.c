// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

#include <stdlib.h>

int numWays(int steps, int arrLen) {
    const int mod = 1000000007;
    int width = arrLen;
    if (width > steps / 2 + 1) width = steps / 2 + 1;
    int* dp = (int*)calloc((size_t)width, sizeof(int));
    dp[0] = 1;
    for (int s = 0; s < steps; s++) {
        int* ndp = (int*)calloc((size_t)width, sizeof(int));
        for (int i = 0; i < width; i++) {
            long long val = dp[i];
            if (i) val += dp[i - 1];
            if (i + 1 < width) val += dp[i + 1];
            ndp[i] = (int)(val % mod);
        }
        free(dp);
        dp = ndp;
    }
    int ans = dp[0];
    free(dp);
    return ans;
}
