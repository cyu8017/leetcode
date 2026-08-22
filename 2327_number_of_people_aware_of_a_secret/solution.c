// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

#include <stdlib.h>

int peopleAwareOfSecret(int n, int delay, int forget) {
    const int mod = 1000000007;
    int* dp = (int*)calloc((size_t)(n + 1), sizeof(int));
    dp[1] = 1;
    int share = 0;
    for (int day = 2; day <= n; day++) {
        if (day - delay >= 1) share = (share + dp[day - delay]) % mod;
        if (day - forget >= 1) share = (share - dp[day - forget] + mod) % mod;
        dp[day] = share;
    }
    int ans = 0;
    for (int day = n - forget + 1; day <= n; day++) {
        if (day >= 1) ans = (ans + dp[day]) % mod;
    }
    free(dp);
    return ans;
}
