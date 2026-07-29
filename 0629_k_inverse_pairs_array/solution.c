// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

#include <stdlib.h>
#include <string.h>

int kInversePairs(int n, int k) {
    const int mod = 1000000007;
    int* dp = (int*)calloc((size_t)k + 1, sizeof(int));
    dp[0] = 1;
    for (int size = 1; size <= n; size++) {
        int* nxt = (int*)calloc((size_t)k + 1, sizeof(int));
        long long prefix = 0;
        for (int pairs = 0; pairs <= k; pairs++) {
            prefix = (prefix + dp[pairs]) % mod;
            if (pairs >= size) {
                prefix = (prefix - dp[pairs - size] + mod) % mod;
            }
            nxt[pairs] = (int)prefix;
        }
        free(dp);
        dp = nxt;
    }
    int answer = dp[k];
    free(dp);
    return answer;
}
