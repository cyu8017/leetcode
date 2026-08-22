// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

#include <string.h>
#include <stdbool.h>

static int digits3966[20], nd3966, K3966;
static long long memo3966[20][10][2];
static char seen3966[20][10][2];

static int abs3966(int x) { return x < 0 ? -x : x; }

static long long dfs3966(int position, int previous, int started, int tight) {
    if (position == nd3966) return started ? 1 : 0;
    if (!tight && started && seen3966[position][previous][started])
        return memo3966[position][previous][started];
    int limit = tight ? digits3966[position] : 9;
    long long result = 0;
    for (int digit = 0; digit <= limit; digit++) {
        int nextStarted = started || digit != 0;
        if (started && abs3966(previous - digit) > K3966) continue;
        int nextPrevious = nextStarted ? digit : previous;
        result += dfs3966(position + 1, nextPrevious, nextStarted, tight && digit == limit);
    }
    if (!tight && started) {
        seen3966[position][previous][started] = 1;
        memo3966[position][previous][started] = result;
    }
    return result;
}

static long long count3966(long long bound) {
    if (bound <= 0) return 0;
    nd3966 = 0;
    long long x = bound;
    int tmp[20]; int tn = 0;
    while (x > 0) { tmp[tn++] = (int)(x % 10); x /= 10; }
    for (int i = tn - 1; i >= 0; i--) digits3966[nd3966++] = tmp[i];
    memset(seen3966, 0, sizeof(seen3966));
    return dfs3966(0, 0, 0, 1);
}

long long countGoodIntegers(long long l, long long r, int k) {
    K3966 = k;
    return count3966(r) - count3966(l - 1);
}
