// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

#include <stdlib.h>
#include <string.h>

static int cmp_ch(const void* a, const void* b) {
    return (*(const unsigned char*)a) - (*(const unsigned char*)b);
}

char* makeAntiPalindrome(char* s) {
    int n = (int)strlen(s);
    char* cs = (char*)malloc((size_t)n + 1);
    memcpy(cs, s, (size_t)n + 1);
    qsort(cs, (size_t)n, 1, cmp_ch);
    int m = n / 2;
    if (cs[m] == cs[m - 1]) {
        int i = m;
        while (i < n && cs[i] == cs[i - 1]) i++;
        for (int j = m; j < n && cs[j] == cs[n - j - 1]; i++, j++) {
            if (i >= n) { free(cs); return "-1"; }
            char tmp = cs[i]; cs[i] = cs[j]; cs[j] = tmp;
        }
    }
    return cs;
}
