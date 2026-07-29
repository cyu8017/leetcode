// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

int numTilings(int n) {
    const int MOD = 1000000007;
    if (n == 1) return 1;
    if (n == 2) return 2;
    long long dp[1001];
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 5;
    for (int i = 4; i <= n; i++) dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD;
    return (int)dp[n];
}
