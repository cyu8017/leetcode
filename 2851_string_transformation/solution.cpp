// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

#include <string>

class Solution {
public:
    int numberOfWays(std::string s, std::string t, long long k) {
        const int MOD = 1000000007;
        int n = (int)s.size();
        std::string ss = s + s;
        if (ss.substr(0, 2 * n - 1).find(t) == std::string::npos) return 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) if (ss.substr(i, n) == t) cnt++;
        auto modPow = [&](long long a, long long b) {
            long long res = 1;
            a %= MOD;
            while (b > 0) {
                if (b & 1) res = res * a % MOD;
                a = a * a % MOD;
                b >>= 1;
            }
            return (int)res;
        };
        int same = (s == t);
        int pk = modPow(n - 1, k);
        int invn = modPow(n, MOD - 2);
        int sign = (k % 2 == 1) ? MOD - 1 : 1;
        int waysSame = (int)((1LL * pk + 1LL * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD);
        int waysDiff = (int)((1LL * pk - sign + MOD) % MOD * invn % MOD);
        if (same) return waysSame;
        return (int)(1LL * waysDiff * cnt % MOD);
    }
};
