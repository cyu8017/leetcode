// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

#include <stdlib.h>

enum { MOD3916 = 1000000007LL };

static long long powmod3916(long long a, long long e) {
    long long res = 1;
    while (e > 0) {
        if (e & 1) res = res * a % MOD3916;
        a = a * a % MOD3916;
        e >>= 1;
    }
    return res;
}

int zigZagArrays(int n, int l, int r) {
    int points = n + 1;
    long long* values = calloc((size_t)(points + 1), sizeof(long long));
    for (int m = 1; m <= points; m++) {
        long long* up = malloc((size_t)m * sizeof(long long));
        long long* down = malloc((size_t)m * sizeof(long long));
        for (int value = 0; value < m; value++) {
            up[value] = value;
            down[value] = m - 1 - value;
        }
        for (int length = 3; length <= n; length++) {
            long long* nextUp = calloc((size_t)m, sizeof(long long));
            long long* nextDown = calloc((size_t)m, sizeof(long long));
            long long prefix = 0;
            for (int value = 0; value < m; value++) {
                nextUp[value] = prefix;
                prefix = (prefix + down[value]) % MOD3916;
            }
            long long suffix = 0;
            for (int value = m - 1; value >= 0; value--) {
                nextDown[value] = suffix;
                suffix = (suffix + up[value]) % MOD3916;
            }
            free(up); free(down);
            up = nextUp; down = nextDown;
        }
        for (int value = 0; value < m; value++) {
            values[m] = (values[m] + up[value] + down[value]) % MOD3916;
        }
        free(up); free(down);
    }
    long long x = (long long)(r - l + 1) % MOD3916;
    if (r - l + 1 <= points) {
        int ans = (int)values[r - l + 1];
        free(values);
        return ans;
    }
    long long* prefix = calloc((size_t)(points + 2), sizeof(long long));
    long long* suffix = calloc((size_t)(points + 2), sizeof(long long));
    prefix[0] = 1;
    for (int i = 1; i <= points; i++)
        prefix[i] = prefix[i - 1] * ((x - i + MOD3916) % MOD3916) % MOD3916;
    suffix[points + 1] = 1;
    for (int i = points; i >= 1; i--)
        suffix[i] = suffix[i + 1] * ((x - i + MOD3916) % MOD3916) % MOD3916;
    long long* factorial = calloc((size_t)(points + 1), sizeof(long long));
    factorial[0] = 1;
    for (int i = 1; i <= points; i++) factorial[i] = factorial[i - 1] * i % MOD3916;
    long long answer = 0;
    for (int i = 1; i <= points; i++) {
        long long numerator = prefix[i - 1] * suffix[i + 1] % MOD3916;
        long long denominator = factorial[i - 1] * factorial[points - i] % MOD3916;
        long long term = values[i] * numerator % MOD3916 * powmod3916(denominator, MOD3916 - 2) % MOD3916;
        if ((points - i) % 2 == 1) answer -= term;
        else answer += term;
        answer %= MOD3916;
    }
    if (answer < 0) answer += MOD3916;
    free(values); free(prefix); free(suffix); free(factorial);
    return (int)answer;
}
