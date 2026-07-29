// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

#include <stdlib.h>
#include <string.h>

int numMusicPlaylists(int n, int goal, int k) {
    const int MOD = 1000000007;
    long long** dp = (long long**)malloc((size_t)(goal + 1) * sizeof(long long*));
    for (int i = 0; i <= goal; i++) {
        dp[i] = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    }
    dp[0][0] = 1;
    for (int i = 1; i <= goal; i++) {
        for (int j = 1; j <= i && j <= n; j++) {
            dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD;
            if (j > k) dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD;
        }
    }
    int ans = (int)dp[goal][n];
    for (int i = 0; i <= goal; i++) free(dp[i]);
    free(dp);
    return ans;
}
