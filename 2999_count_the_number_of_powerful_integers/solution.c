// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static long long dfs2999(int pos, int tight, const char* t, int tlen, const char* s, int sn, int limit, long long* memo, int* seen) {
    if (pos == tlen - sn) {
        const char* suffix = t + pos;
        if (tight) return strcmp(suffix, s) >= 0 ? 1 : 0;
        return 1;
    }
    int key = pos * 2 + tight;
    if (seen[key]) return memo[key];
    int up = limit;
    if (tight) {
        up = t[pos] - '0';
        if (up > limit) up = limit;
    }
    long long ans = 0;
    for (int d = 0; d <= up; d++) {
        int nt = tight && (d == t[pos] - '0');
        ans += dfs2999(pos + 1, nt, t, tlen, s, sn, limit, memo, seen);
    }
    seen[key] = 1;
    memo[key] = ans;
    return ans;
}

static long long count2999(long long num, int limit, const char* s) {
    if (num < 0) return 0;
    char t[32];
    sprintf(t, "%lld", num);
    int tlen = (int)strlen(t);
    int sn = (int)strlen(s);
    if (tlen < sn) return 0;
    long long ans = 0;
    for (int length = sn; length < tlen; length++) {
        int preLen = length - sn;
        long long ways = 1;
        if (preLen > 0) {
            ways = limit;
            for (int i = 1; i < preLen; i++) ways *= (limit + 1);
        }
        ans += ways;
    }
    long long memo[64];
    int seen[64];
    memset(seen, 0, sizeof(seen));
    ans += dfs2999(0, 1, t, tlen, s, sn, limit, memo, seen);
    return ans;
}

long long numberOfPowerfulInt(long long start, long long finish, int limit, char* s) {
    return count2999(finish, limit, s) - count2999(start - 1, limit, s);
}
