// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

#include <stdio.h>
#include <string.h>

static int ipow(int base, int exp) {
    int r = 1;
    while (exp-- > 0) r *= base;
    return r;
}

static int countUpTo(char** digits, int digitsSize, const char* s) {
    int len = (int)strlen(s);
    if (len == 0) return 0;
    int first = 0;
    for (int i = 0; i < digitsSize; i++) {
        if (digits[i][0] < s[0]) first++;
    }
    int ways = first * ipow(digitsSize, len - 1);
    int found = 0;
    for (int i = 0; i < digitsSize; i++) {
        if (digits[i][0] == s[0]) { found = 1; break; }
    }
    if (found) ways += countUpTo(digits, digitsSize, s + 1);
    return ways;
}

int atMostNGivenDigitSet(char** digits, int digitsSize, int n) {
    char s[12];
    sprintf(s, "%d", n);
    int m = (int)strlen(s);
    int ans = 0;
    for (int i = 1; i < m; i++) ans += ipow(digitsSize, i);
    ans += countUpTo(digits, digitsSize, s);
    return ans;
}
