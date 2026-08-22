// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

#include <stdlib.h>
#include <string.h>

#define MAX3518 1000001

static int nCk(int n, int kk) {
    if (kk < 0 || kk > n) return 0;
    long long res = 1;
    if (kk > n - kk) kk = n - kk;
    for (int i = 1; i <= kk; i++) {
        res = res * (n - i + 1) / i;
        if (res >= MAX3518) return MAX3518;
    }
    return (int)res;
}

static int countArr(int* h) {
    int total = 0;
    for (int i = 0; i < 26; i++) total += h[i];
    long long res = 1;
    for (int i = 0; i < 26; i++) {
        int f = h[i];
        res *= nCk(total, f);
        if (res >= MAX3518) return MAX3518;
        total -= f;
    }
    return (int)res;
}

char* smallestPalindrome(char* s, int k) {
    int cnt[26] = {0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    int odd = 0;
    for (int i = 0; i < 26; i++) if (cnt[i] % 2) odd++;
    if (odd > 1) {
        char* empty = (char*)malloc(1); empty[0] = '\0'; return empty;
    }
    int half[26];
    char mid = 0;
    for (int i = 0; i < 26; i++) {
        half[i] = cnt[i] / 2;
        if (cnt[i] % 2) mid = (char)('a' + i);
    }
    if (countArr(half) < k) {
        char* empty = (char*)malloc(1); empty[0] = '\0'; return empty;
    }
    int halfLen = 0;
    for (int i = 0; i < 26; i++) halfLen += half[i];
    char* left = (char*)malloc((size_t)halfLen + 1);
    int ll = 0;
    for (int t = 0; t < halfLen; t++) {
        for (int i = 0; i < 26; i++) {
            if (half[i] == 0) continue;
            half[i]--;
            int arr = countArr(half);
            if (arr >= k) {
                left[ll++] = (char)('a' + i);
                break;
            }
            k -= arr;
            half[i]++;
        }
    }
    int total = ll * 2 + (mid ? 1 : 0);
    char* res = (char*)malloc((size_t)total + 1);
    int oi = 0;
    for (int i = 0; i < ll; i++) res[oi++] = left[i];
    if (mid) res[oi++] = mid;
    for (int i = ll - 1; i >= 0; i--) res[oi++] = left[i];
    res[oi] = '\0';
    free(left);
    return res;
}
