// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

#include <stdlib.h>
#include <string.h>

static int gcd3336(int a, int b) {
    if (a == 0) return b;
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int subsequencePairCount(int* nums, int numsSize) {
    const int mod = 1000000007;
    int maxV = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxV) maxV = nums[i];
    int** dp = (int**)malloc((size_t)(maxV + 1) * sizeof(int*));
    for (int i = 0; i <= maxV; i++) dp[i] = (int*)calloc((size_t)(maxV + 1), sizeof(int));
    dp[0][0] = 1;
    for (int ti = 0; ti < numsSize; ti++) {
        int x = nums[ti];
        int** ndp = (int**)malloc((size_t)(maxV + 1) * sizeof(int*));
        for (int i = 0; i <= maxV; i++) {
            ndp[i] = (int*)malloc((size_t)(maxV + 1) * sizeof(int));
            memcpy(ndp[i], dp[i], (size_t)(maxV + 1) * sizeof(int));
        }
        for (int a = 0; a <= maxV; a++) {
            for (int b = 0; b <= maxV; b++) {
                if (!dp[a][b]) continue;
                int na = a == 0 ? x : gcd3336(a, x);
                int nb = b == 0 ? x : gcd3336(b, x);
                ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod;
                ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod;
            }
        }
        for (int i = 0; i <= maxV; i++) free(dp[i]);
        free(dp); dp = ndp;
    }
    int ans = 0;
    for (int g = 1; g <= maxV; g++) ans = (ans + dp[g][g]) % mod;
    for (int i = 0; i <= maxV; i++) free(dp[i]);
    free(dp);
    return ans;
}
