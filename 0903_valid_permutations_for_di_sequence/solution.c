// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

#include <stdlib.h>
#include <string.h>

int numPermsDISequence(char* s) {
    const int MOD = 1000000007;
    int n = (int)strlen(s);
    int* dp = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i <= n; i++) dp[i] = 1;
    for (int i = 1; i <= n; i++) {
        int* new_dp = (int*)calloc((size_t)(n + 1), sizeof(int));
        if (s[i - 1] == 'I') {
            int postfix = 0;
            for (int j = n - i; j >= 0; j--) {
                postfix = (postfix + dp[j + 1]) % MOD;
                new_dp[j] = postfix;
            }
        } else {
            int prefix = 0;
            for (int j = 0; j <= n - i; j++) {
                prefix = (prefix + dp[j]) % MOD;
                new_dp[j] = prefix;
            }
        }
        free(dp);
        dp = new_dp;
    }
    int ans = dp[0];
    free(dp);
    return ans;
}
