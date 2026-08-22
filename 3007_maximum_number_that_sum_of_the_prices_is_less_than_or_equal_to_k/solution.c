// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

#include <string.h>
#include <stdbool.h>

static long long num3007;
static long long f3007[65][65];
static int x3007;

static int bitlen(unsigned long long n) {
    int c = 0;
    while (n) { c++; n >>= 1; }
    return c;
}

static long long dfs3007(int pos, int cnt, bool limit) {
    if (pos == 0) return cnt;
    if (!limit && f3007[pos][cnt] != -1) return f3007[pos][cnt];
    long long ans = 0;
    int up = limit ? (int)((num3007 >> (pos - 1)) & 1) : 1;
    for (int i = 0; i <= up; i++) {
        int v = cnt;
        if (i == 1 && pos % x3007 == 0) v++;
        ans += dfs3007(pos - 1, v, limit && i == up);
    }
    if (!limit) f3007[pos][cnt] = ans;
    return ans;
}

long long findMaximumNumber(long long k, int x) {
    x3007 = x;
    long long l = 1, r = (long long)1e17;
    while (l < r) {
        long long mid = (l + r + 1) >> 1;
        num3007 = mid;
        int m = bitlen((unsigned long long)num3007);
        memset(f3007, -1, sizeof(f3007));
        if (dfs3007(m, 0, true) <= k) l = mid;
        else r = mid - 1;
    }
    return l;
}
