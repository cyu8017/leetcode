// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

#define NEG3466 (-(1LL << 60))

static long long max64_3466(long long a, long long b) { return a > b ? a : b; }

long long maxCoins(int* lane1, int lane1Size, int* lane2, int lane2Size) {
    (void)lane2Size;
    int n = lane1Size;
    long long dp[2][2];
    dp[0][0] = lane1[0];
    dp[1][0] = lane2[0];
    dp[0][1] = NEG3466;
    dp[1][1] = NEG3466;
    long long ans = dp[0][0];
    if (dp[1][0] > ans) ans = dp[1][0];
    for (int i = 1; i < n; i++) {
        long long ndp[2][2];
        ndp[0][0] = max64_3466(dp[0][0], 0) + lane1[i];
        ndp[1][0] = max64_3466(dp[1][0], 0) + lane2[i];
        ndp[0][1] = max64_3466(dp[0][1], dp[1][0]) + lane1[i];
        ndp[1][1] = max64_3466(dp[1][1], dp[0][0]) + lane2[i];
        if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i];
        if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i];
        dp[0][0] = ndp[0][0];
        dp[0][1] = ndp[0][1];
        dp[1][0] = ndp[1][0];
        dp[1][1] = ndp[1][1];
        for (int a = 0; a < 2; a++)
            for (int b = 0; b < 2; b++)
                if (dp[a][b] > ans) ans = dp[a][b];
    }
    return ans;
}
