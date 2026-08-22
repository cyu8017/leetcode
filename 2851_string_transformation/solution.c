// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

#include <stdlib.h>
#include <string.h>

static long long modPow(long long a, long long b) {
    const int mod = 1000000007;
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

int numberOfWays(char* s, char* t, long long k) {
    const int mod = 1000000007;
    int n = (int)strlen(s);
    char* ss = (char*)malloc(2 * n + 1);
    memcpy(ss, s, n);
    memcpy(ss + n, s, n);
    ss[2 * n] = 0;
    // check t is rotation of s
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (strncmp(ss + i, t, n) == 0) { found = 1; break; }
    }
    if (!found) { free(ss); return 0; }
    int cnt = 0;
    for (int i = 0; i < n; i++)
        if (strncmp(ss + i, t, n) == 0) cnt++;
    int same = strcmp(s, t) == 0 ? 1 : 0;
    long long pk = modPow(n - 1, k);
    long long invn = modPow(n, mod - 2);
    long long sign = (k % 2 == 1) ? (mod - 1) : 1;
    long long waysSame = (pk + (n - 1) % mod * sign % mod) % mod * invn % mod;
    long long waysDiff = (pk - sign + mod) % mod * invn % mod;
    free(ss);
    if (same) return (int)waysSame;
    return (int)(waysDiff * cnt % mod);
}
