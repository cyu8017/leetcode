// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int isPal(long long x) {
    char buf[24];
    sprintf(buf, "%lld", x);
    int n = (int)strlen(buf);
    for (int i = 0; i < n / 2; i++) if (buf[i] != buf[n - 1 - i]) return 0;
    return 1;
}

static long long makeEven(long long k) {
    char s[12], buf[24];
    sprintf(s, "%lld", k);
    int n = (int)strlen(s);
    strcpy(buf, s);
    for (int i = 0; i < n; i++) buf[n + i] = s[n - 1 - i];
    buf[2 * n] = 0;
    return atoll(buf);
}

static long long makeOdd(long long k) {
    char s[12], buf[24];
    sprintf(s, "%lld", k);
    int n = (int)strlen(s);
    strcpy(buf, s);
    for (int i = 0; i < n - 1; i++) buf[n + i] = s[n - 2 - i];
    buf[2 * n - 1] = 0;
    return atoll(buf);
}

int superpalindromesInRange(char* left, char* right) {
    long long L = atoll(left), R = atoll(right);
    int ans = 0;
    for (long long k = 1; k <= 100000; k++) {
        long long pal = makeEven(k);
        long long sq = pal * pal;
        if (sq > R) break;
        if (sq >= L && isPal(sq)) ans++;
    }
    for (long long k = 1; k <= 100000; k++) {
        long long pal = makeOdd(k);
        long long sq = pal * pal;
        if (sq > R) break;
        if (sq >= L && isPal(sq)) ans++;
    }
    return ans;
}
