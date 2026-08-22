// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

#include <stdlib.h>
#include <string.h>

int goodBinaryStrings(int minLength, int maxLength, int oneGroup, int zeroGroup) {
    const int MOD = 1000000007;
    int* dp = (int*)calloc((size_t)(maxLength + 1), sizeof(int));
    dp[0] = 1;
    for (int i = 0; i <= maxLength; i++) {
        if (!dp[i]) continue;
        if (i + oneGroup <= maxLength) dp[i + oneGroup] = (dp[i + oneGroup] + dp[i]) % MOD;
        if (i + zeroGroup <= maxLength) dp[i + zeroGroup] = (dp[i + zeroGroup] + dp[i]) % MOD;
    }
    int ans = 0;
    for (int i = minLength; i <= maxLength; i++) ans = (ans + dp[i]) % MOD;
    free(dp);
    return ans;
}
