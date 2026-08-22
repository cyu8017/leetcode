// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool dfs3348(char* res, int L, int i, bool tight, bool sameLen, const char* num, long long t) {
    if (i == L) {
        long long prod = 1;
        for (int j = 0; j < L; j++) { prod *= (res[j] - '0'); if (prod == 0) break; }
        return prod % t == 0 && prod > 0;
    }
    char start = i == 0 ? '1' : '0';
    int nlen = (int)strlen(num);
    if (tight && sameLen && i < nlen) start = num[i];
    for (char c = start; c <= '9'; c++) {
        res[i] = c;
        bool nt = tight && sameLen && i < nlen && c == num[i];
        if (dfs3348(res, L, i + 1, nt, sameLen, num, t)) return true;
    }
    return false;
}

char* smallestNumber(char* num, long long t) {
    long long tt = t;
    for (int d = 9; d >= 2; d--) while (tt % d == 0) tt /= d;
    char* neg = (char*)malloc(3); strcpy(neg, "-1");
    if (tt > 1) return neg;
    int nlen = (int)strlen(num);
    for (int extra = 0; extra <= 60; extra++) {
        int L = nlen + extra;
        char* res = (char*)malloc(L + 1); res[L] = 0;
        if (dfs3348(res, L, 0, true, extra == 0, num, t)) { free(neg); return res; }
        free(res);
    }
    return neg;
}
