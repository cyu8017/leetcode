// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

#include <cstdint>

class Solution {
    static constexpr int MX = 500001;
    static constexpr int64_t MOD = 1000000007LL;

    static int64_t f[MX];
    static int64_t g[MX];
    static bool inited;

    static int64_t modPow(int64_t a, int64_t b) {
        int64_t res = 1;
        a %= MOD;
        while (b > 0) {
            if (b & 1) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    static void ensureInit() {
        if (inited) return;
        inited = true;
        f[0] = 1;
        g[0] = 1;
        for (int i = 1; i < MX; i++) {
            f[i] = f[i - 1] * (int64_t)i % MOD;
            g[i] = modPow(f[i], MOD - 2);
        }
    }

    static int64_t comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        return f[n] * g[k] % MOD * g[n - k] % MOD;
    }

public:
    int countValidSequences(int n, int k) {
        ensureInit();
        int64_t ans = comb(n - 1, k - 1);
        if ((n + k) % 2 == 0) {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        }
        return (int)ans;
    }
};

int64_t Solution::f[Solution::MX];
int64_t Solution::g[Solution::MX];
bool Solution::inited = false;
