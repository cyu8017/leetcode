// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int countBinaryPalindromes(long long n) {
    if (n == 0) return 1;
    int ans = 1;
    char s[70];
    // format binary
    unsigned long long un = (unsigned long long)n;
    int L = 0;
    unsigned long long tmp = un;
    char rev[70];
    if (tmp == 0) { s[0] = '0'; s[1] = 0; L = 1; }
    else {
        while (tmp) { rev[L++] = (char)('0' + (tmp & 1)); tmp >>= 1; }
        for (int i = 0; i < L; i++) s[i] = rev[L - 1 - i];
        s[L] = 0;
    }
    for (int len_ = 1; len_ < L; len_++) {
        int half = (len_ + 1) / 2;
        ans += 1 << (half - 1);
    }
    int half = (L + 1) / 2;
    char prefix[70];
    memcpy(prefix, s, (size_t)half);
    prefix[half] = 0;
    int start = 1 << (half - 1);
    long long prefVal = 0;
    for (int i = 0; i < half; i++) prefVal = (prefVal << 1) | (prefix[i] - '0');
    ans += (int)prefVal - start;
    char pal[70];
    int pn = 0;
    for (int i = 0; i < half; i++) pal[pn++] = prefix[i];
    for (int i = half - 1 - (L % 2); i >= 0; i--) pal[pn++] = prefix[i];
    pal[pn] = 0;
    long long pval = 0;
    for (int i = 0; i < pn; i++) pval = (pval << 1) | (pal[i] - '0');
    if (pval <= n) ans++;
    return ans;
}
