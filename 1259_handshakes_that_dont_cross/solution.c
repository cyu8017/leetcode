// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

#include <stdlib.h>

int numberOfWays(int numPeople) {
    const int mod = 1000000007;
    int* dp = (int*)calloc((size_t)numPeople + 1, sizeof(int));
    dp[0] = 1;
    for (int people = 2; people <= numPeople; people += 2) {
        for (int left = 0; left < people; left += 2) {
            dp[people] = (dp[people] + (long long)dp[left] * dp[people - 2 - left]) % mod;
        }
    }
    int ans = dp[numPeople];
    free(dp);
    return ans;
}
