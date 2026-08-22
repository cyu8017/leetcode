// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

static bool check3869(int s) {
    if (s < 100) return s % 11 != 0;
    int mid = (s / 10) % 10;
    int last = s % 10;
    return mid > 1 && mid < last;
}

static char num3869[32];
static int n3869;
static long long**** f3869;
static int f_n3869;

static long long dfs3869(int pos, int s, int prev, int st, bool lim) {
    if (pos >= n3869) {
        if (st != 3) return 1;
        return check3869(s) ? 1 : 0;
    }
    if (!lim && f3869[pos][s][prev][st] != -1) return f3869[pos][s][prev][st];
    int up = lim ? (num3869[pos] - '0') : 9;
    long long res = 0;
    for (int i = 0; i <= up; i++) {
        int nxtSt = st;
        if (st == 0) {
            if (prev == 0) nxtSt = 0;
            else if (i > prev) nxtSt = 1;
            else if (i < prev) nxtSt = 2;
            else nxtSt = 3;
        } else if (st == 1) nxtSt = (i > prev) ? 1 : 3;
        else if (st == 2) nxtSt = (i < prev) ? 2 : 3;
        else nxtSt = 3;
        res += dfs3869(pos + 1, s + i, i, nxtSt, lim && i == up);
    }
    if (!lim) f3869[pos][s][prev][st] = res;
    return res;
}

static void free_f3869(void) {
    if (!f3869) return;
    for (int i = 0; i < f_n3869; i++) {
        for (int j = 0; j <= 9 * f_n3869; j++) {
            for (int k = 0; k < 10; k++) free(f3869[i][j][k]);
            free(f3869[i][j]);
        }
        free(f3869[i]);
    }
    free(f3869);
    f3869 = NULL;
}

static long long calc3869(long long x) {
    sprintf(num3869, "%lld", x);
    n3869 = (int)strlen(num3869);
    free_f3869();
    f_n3869 = n3869;
    f3869 = (long long****)malloc((size_t)n3869 * sizeof(long long***));
    for (int i = 0; i < n3869; i++) {
        f3869[i] = (long long***)malloc((size_t)(9 * n3869 + 1) * sizeof(long long**));
        for (int j = 0; j <= 9 * n3869; j++) {
            f3869[i][j] = (long long**)malloc(10 * sizeof(long long*));
            for (int k = 0; k < 10; k++) {
                f3869[i][j][k] = (long long*)malloc(4 * sizeof(long long));
                for (int t = 0; t < 4; t++) f3869[i][j][k][t] = -1;
            }
        }
    }
    return dfs3869(0, 0, 0, 0, true);
}

long long countFancy(long long l, long long r) {
    long long ans = calc3869(r) - calc3869(l - 1);
    free_f3869();
    return ans;
}
