// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isPrime2478(char c) {
    return c == '2' || c == '3' || c == '5' || c == '7';
}

int beautifulPartitions(char* s, int k, int minLength) {
    const int mod = 1000000007;
    int n = (int)strlen(s);
    if (!isPrime2478(s[0]) || isPrime2478(s[n - 1])) return 0;
    int** dp = (int**)malloc((size_t)(k + 1) * sizeof(int*));
    for (int i = 0; i <= k; i++) dp[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    dp[0][0] = 1;
    for (int p = 1; p <= k; p++) {
        int pref = 0, j = 0;
        for (int i = 1; i <= n; i++) {
            while (j <= i - minLength) {
                if (j == 0 || (isPrime2478(s[j]) && !isPrime2478(s[j - 1])))
                    pref = (pref + dp[p - 1][j]) % mod;
                j++;
            }
            if (!isPrime2478(s[i - 1])) dp[p][i] = pref;
        }
    }
    int ans = dp[k][n];
    for (int i = 0; i <= k; i++) free(dp[i]);
    free(dp);
    return ans;
}
