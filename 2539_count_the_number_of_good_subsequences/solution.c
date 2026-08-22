// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

#include <stdlib.h>
#include <string.h>

enum { MOD2539 = 1000000007 };

static long long modPow2539(long long a, long long e) {
    long long res = 1;
    while (e > 0) {
        if (e & 1) res = res * a % MOD2539;
        a = a * a % MOD2539;
        e >>= 1;
    }
    return res;
}

int countGoodSubsequences(char* s) {
    int cnt[26] = {0}, maxf = 0;
    for (int i = 0; s[i]; i++) {
        cnt[s[i] - 'a']++;
        if (cnt[s[i] - 'a'] > maxf) maxf = cnt[s[i] - 'a'];
    }
    long long* fact = (long long*)malloc((size_t)(maxf + 1) * sizeof(long long));
    long long* invFact = (long long*)malloc((size_t)(maxf + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= maxf; i++) fact[i] = fact[i - 1] * i % MOD2539;
    invFact[maxf] = modPow2539(fact[maxf], MOD2539 - 2);
    for (int i = maxf; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD2539;
    long long ans = 0;
    for (int k = 1; k <= maxf; k++) {
        long long ways = 1;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] >= k) {
                long long c = fact[cnt[i]] * invFact[k] % MOD2539 * invFact[cnt[i] - k] % MOD2539;
                ways = ways * (1 + c) % MOD2539;
            }
        }
        ans = (ans + ways - 1 + MOD2539) % MOD2539;
    }
    free(fact); free(invFact);
    return (int)ans;
}
