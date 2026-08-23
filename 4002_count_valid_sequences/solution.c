// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

#include <stdint.h>

#define MX4002 500001
#define MOD4002 1000000007LL

static int64_t f4002[MX4002];
static int64_t g4002[MX4002];
static int init4002 = 0;

static int64_t modPow4002(int64_t a, int64_t b) {
    int64_t res = 1;
    a %= MOD4002;
    while (b > 0) {
        if (b & 1) res = res * a % MOD4002;
        a = a * a % MOD4002;
        b >>= 1;
    }
    return res;
}

static void ensureInit4002(void) {
    if (init4002) return;
    init4002 = 1;
    f4002[0] = 1;
    g4002[0] = 1;
    for (int i = 1; i < MX4002; i++) {
        f4002[i] = f4002[i - 1] * (int64_t)i % MOD4002;
        g4002[i] = modPow4002(f4002[i], MOD4002 - 2);
    }
}

static int64_t comb4002(int n, int k) {
    if (k < 0 || k > n) return 0;
    return f4002[n] * g4002[k] % MOD4002 * g4002[n - k] % MOD4002;
}

int countValidSequences(int n, int k) {
    ensureInit4002();
    int64_t ans = comb4002(n - 1, k - 1);
    if ((n + k) % 2 == 0) {
        ans = (ans - comb4002((n + k) / 2 - 1, k - 1) + MOD4002) % MOD4002;
    }
    return (int)ans;
}
