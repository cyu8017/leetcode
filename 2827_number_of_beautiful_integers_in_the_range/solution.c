// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static char S2827[20];
static int N2827, K2827;
static int memo2827[12][42][22][2][2];

static int dfs2827(int pos, int diff, int mod, int tight, int started) {
    if (pos == N2827) return (started && diff == 0 && mod == 0) ? 1 : 0;
    int* cell = &memo2827[pos][diff + 20][mod][tight][started];
    if (*cell != -1) return *cell;
    int up = tight ? (S2827[pos] - '0') : 9;
    int ans = 0;
    for (int d = 0; d <= up; d++) {
        int nt = tight && (d == up);
        if (!started) {
            if (d == 0) ans += dfs2827(pos + 1, diff, mod, nt, 0);
            else {
                int nd = diff + ((d % 2 == 0) ? 1 : -1);
                ans += dfs2827(pos + 1, nd, d % K2827, nt, 1);
            }
        } else {
            int nd = diff + ((d % 2 == 0) ? 1 : -1);
            ans += dfs2827(pos + 1, nd, (mod * 10 + d) % K2827, nt, 1);
        }
    }
    return *cell = ans;
}

static int count2827(int n) {
    if (n < 0) return 0;
    sprintf(S2827, "%d", n);
    N2827 = (int)strlen(S2827);
    memset(memo2827, -1, sizeof(memo2827));
    return dfs2827(0, 0, 0, 1, 0);
}

int numberOfBeautifulIntegers(int low, int high, int k) {
    K2827 = k;
    return count2827(high) - count2827(low - 1);
}
