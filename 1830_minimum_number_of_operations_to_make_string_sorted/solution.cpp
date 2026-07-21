// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

#include <string>
#include <vector>

class Solution {
public:
    int makeStringSorted(std::string s) {
        const int MOD = 1000000007;
        int n = static_cast<int>(s.size());
        std::vector<long long> fact(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        std::vector<long long> invFact(n + 1, 1);
        invFact[n] = powMod(fact[n], MOD - 2, MOD);
        for (int i = n - 1; i >= 0; --i) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;
        }

        std::vector<int> freq(26, 0);
        for (char ch : s) {
            freq[ch - 'a'] += 1;
        }

        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            for (int smaller = 0; smaller < c; ++smaller) {
                if (freq[smaller] == 0) {
                    continue;
                }
                freq[smaller] -= 1;
                long long ways = fact[n - i - 1];
                for (int count : freq) {
                    ways = ways * invFact[count] % MOD;
                }
                ans = (ans + ways) % MOD;
                freq[smaller] += 1;
            }
            freq[c] -= 1;
        }
        return static_cast<int>(ans);
    }

private:
    long long powMod(long long base, long long exp, long long mod) {
        long long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) {
                result = result * base % mod;
            }
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }
};
