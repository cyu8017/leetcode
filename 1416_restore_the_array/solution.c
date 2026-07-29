// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

#include <stdlib.h>
#include <string.h>

int numberOfArrays(char* s, int k) {
    const int MOD = 1000000007;
    int n = (int)strlen(s);
    int* dp = (int*)calloc(n + 1, sizeof(int));
    dp[n] = 1;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '0') continue;
        long long value = 0;
        for (int j = i; j < n; j++) {
            value = value * 10 + (s[j] - '0');
            if (value > k) break;
            dp[i] = (dp[i] + dp[j + 1]) % MOD;
        }
    }
    int ans = dp[0];
    free(dp);
    return ans;
}
