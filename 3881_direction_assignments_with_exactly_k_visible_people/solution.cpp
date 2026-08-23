// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

#include <algorithm>
#include <vector>

class Solution {
    static constexpr int N = 100001;
    static constexpr int MOD = 1000000007;
    static inline std::vector<long long> fact;
    static inline std::vector<long long> invFact;
    static inline bool ready = false;

    static long long qmi(long long a, long long k, long long p) {
        long long res = 1;
        while (k) {
            if (k & 1) res = res * a % p;
            k >>= 1;
            a = a * a % p;
        }
        return res;
    }

    static void init() {
        if (ready) return;
        fact.assign(N, 0);
        invFact.assign(N, 0);
        fact[0] = invFact[0] = 1;
        for (int i = 1; i < N; i++) {
            fact[i] = fact[i - 1] * i % MOD;
            invFact[i] = qmi(fact[i], MOD - 2, MOD);
        }
        ready = true;
    }

    static long long comb(int n, int k) {
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }

public:
    int countVisiblePeople(int n, int pos, int k) {
        init();
        int l = pos, r = n - pos - 1;
        long long ans = 0;
        for (int a = 0; a <= std::min(k, l); a++) {
            int b = k - a;
            if (b <= r) {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD;
            }
        }
        return (int)ans;
    }
};
