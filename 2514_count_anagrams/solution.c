// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

#include <stdlib.h>
#include <string.h>

enum { MOD2514 = 1000000007 };

static long long modPow2514(long long a, long long e) {
    long long res = 1;
    a %= MOD2514;
    while (e > 0) {
        if (e & 1) res = res * a % MOD2514;
        a = a * a % MOD2514;
        e >>= 1;
    }
    return res;
}

int countAnagrams(char* s) {
    int maxN = 0, n = (int)strlen(s);
    int cur = 0;
    for (int i = 0; i <= n; i++) {
        if (i < n && s[i] != ' ') cur++;
        else {
            if (cur > maxN) maxN = cur;
            cur = 0;
        }
    }
    long long* fact = (long long*)malloc((size_t)(maxN + 1) * sizeof(long long));
    long long* invFact = (long long*)malloc((size_t)(maxN + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD2514;
    invFact[maxN] = modPow2514(fact[maxN], MOD2514 - 2);
    for (int i = maxN; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD2514;
    long long ans = 1;
    int i = 0;
    while (i < n) {
        while (i < n && s[i] == ' ') i++;
        if (i >= n) break;
        int cnt[26] = {0};
        int len = 0;
        while (i < n && s[i] != ' ') {
            cnt[s[i] - 'a']++;
            len++;
            i++;
        }
        long long curv = fact[len];
        for (int c = 0; c < 26; c++) curv = curv * invFact[cnt[c]] % MOD2514;
        ans = ans * curv % MOD2514;
    }
    free(fact); free(invFact);
    return (int)ans;
}
