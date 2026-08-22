// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

#include <stdlib.h>
#include <string.h>

static int cmp_desc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}
static int modPow(long long a, long long b) {
    const int mod = 1000000007;
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return (int)res;
}
static int comb(int n, int r) {
    const int mod = 1000000007;
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < r; i++) {
        num = num * (n - i) % mod;
        den = den * (i + 1) % mod;
    }
    return (int)(num * modPow(den, mod - 2) % mod);
}

int countKSubsequencesWithMaxBeauty(char* s, int k) {
    const int mod = 1000000007;
    int freq[26] = {0};
    for (int i = 0; s[i]; i++) freq[s[i] - 'a']++;
    int vals[26], vcnt = 0;
    for (int i = 0; i < 26; i++) if (freq[i] > 0) vals[vcnt++] = freq[i];
    if (vcnt < k) return 0;
    qsort(vals, vcnt, sizeof(int), cmp_desc);
    int threshold = vals[k - 1];
    int need = 0, avail = 0;
    long long prod = 1;
    for (int i = 0; i < vcnt; i++) {
        if (vals[i] > threshold) { prod = prod * vals[i] % mod; need++; }
        else if (vals[i] == threshold) avail++;
    }
    int remain = k - need;
    prod = prod * comb(avail, remain) % mod;
    for (int i = 0; i < remain; i++) prod = prod * threshold % mod;
    return (int)prod;
}
