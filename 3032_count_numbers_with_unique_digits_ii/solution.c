// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

static char num3032[12];
static int f3032[12][1 << 10];
static int nlen3032;

static int dfs3032(int pos, int mask, bool limit) {
    if (pos >= nlen3032) return mask != 0 ? 1 : 0;
    if (!limit && f3032[pos][mask] != -1) return f3032[pos][mask];
    int up = limit ? num3032[pos] - '0' : 9;
    int ans = 0;
    for (int i = 0; i <= up; i++) {
        if ((mask >> i) & 1) continue;
        int nxt = mask | (1 << i);
        if (mask == 0 && i == 0) nxt = 0;
        ans += dfs3032(pos + 1, nxt, limit && i == up);
    }
    if (!limit) f3032[pos][mask] = ans;
    return ans;
}

static int count_to(int x) {
    if (x < 0) return 0;
    sprintf(num3032, "%d", x);
    nlen3032 = (int)strlen(num3032);
    memset(f3032, -1, sizeof(f3032));
    return dfs3032(0, 0, true);
}

int numberCount(int a, int b) {
    return count_to(b) - count_to(a - 1);
}
