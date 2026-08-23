// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

#include <string>
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;
    long long modPow(long long a, long long e) {
        long long res = 1;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
public:
    int countGoodSubsequences(std::string s) {
        int cnt[26] = {};
        int maxf = 0;
        for (char c : s) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] > maxf) maxf = cnt[c - 'a'];
        }
        std::vector<long long> fact(maxf + 1), invFact(maxf + 1);
        fact[0] = 1;
        for (int i = 1; i <= maxf; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxf] = modPow(fact[maxf], MOD - 2);
        for (int i = maxf; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        auto comb = [&](int n, int k) -> long long {
            if (k < 0 || k > n) return 0;
            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
        };
        long long ans = 0;
        for (int k = 1; k <= maxf; k++) {
            long long ways = 1;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] >= k) ways = ways * (1 + comb(cnt[i], k)) % MOD;
            }
            ans = (ans + ways - 1 + MOD) % MOD;
        }
        return (int)ans;
    }
};
