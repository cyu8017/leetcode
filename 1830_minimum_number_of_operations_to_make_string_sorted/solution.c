// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

#include <stdlib.h>
#include <string.h>

static long long powMod(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}

int makeStringSorted(char* s) {
    const long long MOD = 1000000007LL;
    int n = (int)strlen(s);
    long long* fact = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    long long* invFact = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[n] = powMod(fact[n], MOD - 2, MOD);
    for (int i = n - 1; i >= 0; i--) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

    int freq[26] = {0};
    for (int i = 0; i < n; i++) freq[s[i] - 'a']++;

    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        for (int smaller = 0; smaller < c; smaller++) {
            if (freq[smaller] == 0) continue;
            freq[smaller]--;
            long long ways = fact[n - i - 1];
            for (int j = 0; j < 26; j++) ways = ways * invFact[freq[j]] % MOD;
            ans = (ans + ways) % MOD;
            freq[smaller]++;
        }
        freq[c]--;
    }

    free(fact);
    free(invFact);
    return (int)ans;
}
