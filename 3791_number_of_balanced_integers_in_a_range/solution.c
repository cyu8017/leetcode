// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

enum { BASE3791 = 90 };

static char num3791[32];
static long long f3791[20][181];
static int numLen3791;

static long long dfs3791(int pos, int diff, bool lim) {
    if (pos >= numLen3791) return diff == 0 ? 1 : 0;
    if (!lim && f3791[pos][diff + BASE3791] != -1) return f3791[pos][diff + BASE3791];
    int up = lim ? (num3791[pos] - '0') : 9;
    long long res = 0;
    for (int i = 0; i <= up; i++) {
        if (pos % 2 == 0) res += dfs3791(pos + 1, diff + i, lim && i == up);
        else res += dfs3791(pos + 1, diff - i, lim && i == up);
    }
    if (!lim) f3791[pos][diff + BASE3791] = res;
    return res;
}

static long long calc3791(long long x) {
    sprintf(num3791, "%lld", x);
    numLen3791 = (int)strlen(num3791);
    memset(f3791, -1, sizeof(f3791));
    return dfs3791(0, 0, true);
}

long long countBalanced(long long low, long long high) {
    if (high < 11) return 0;
    if (low < 11) low = 11;
    return calc3791(high) - calc3791(low - 1);
}
