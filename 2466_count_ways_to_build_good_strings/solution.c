// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

#include <stdlib.h>
#include <string.h>

int countGoodStrings(int low, int high, int zero, int one) {
    const int mod = 1000000007;
    int* dp = (int*)calloc((size_t)(high + 1), sizeof(int));
    dp[0] = 1;
    int ans = 0;
    for (int i = 1; i <= high; i++) {
        if (i >= zero) dp[i] = (dp[i] + dp[i - zero]) % mod;
        if (i >= one) dp[i] = (dp[i] + dp[i - one]) % mod;
        if (i >= low) ans = (ans + dp[i]) % mod;
    }
    free(dp);
    return ans;
}
