// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

#include <string.h>
#include <stdbool.h>
#include <stdio.h>

static bool key3906[16];
static char s3906[17];
static long long f3906[16][10];

static long long dfs3906(int pos, int last, bool lim) {
    if (pos == 16) return 1;
    if (!lim && f3906[pos][last] != -1) return f3906[pos][last];
    long long res = 0;
    int start = key3906[pos] ? last : 0;
    int end = lim ? (s3906[pos] - '0') : 9;
    for (int i = start; i <= end; i++) {
        int nextLast = key3906[pos] ? i : last;
        res += dfs3906(pos + 1, nextLast, lim && (i == end));
    }
    if (!lim) f3906[pos][last] = res;
    return res;
}

static long long calc3906(long long x) {
    if (x < 0) return 0;
    char t[32];
    snprintf(t, sizeof(t), "%lld", x);
    int len = (int)strlen(t);
    memset(s3906, '0', 16);
    s3906[16] = 0;
    if (len > 16) len = 16;
    memcpy(s3906 + 16 - len, t, (size_t)len);
    for (int i = 0; i < 16; i++)
        for (int j = 0; j < 10; j++) f3906[i][j] = -1;
    return dfs3906(0, 0, true);
}

long long countGoodIntegersOnPath(long long l, long long r, char* directions) {
    memset(key3906, 0, sizeof(key3906));
    int row = 0, col = 0;
    key3906[0] = true;
    for (int i = 0; directions[i]; i++) {
        if (directions[i] == 'D') row++; else col++;
        key3906[row * 4 + col] = true;
    }
    return calc3906(r) - calc3906(l - 1);
}
