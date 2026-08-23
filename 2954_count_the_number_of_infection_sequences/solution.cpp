// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

#include <vector>

class Solution {
public:
    int numberOfSequence(int n, std::vector<int>& sick) {
        const int mod = 1000000007;
        std::vector<int> fact(n + 1), invFact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = 1LL * fact[i - 1] * i % mod;
        auto modPow = [&](long long a, int b) {
            long long res = 1;
            while (b > 0) {
                if (b & 1) res = res * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)res;
        };
        invFact[n] = modPow(fact[n], mod - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = 1LL * invFact[i] * i % mod;
        int m = (int)sick.size();
        int totalEmpty = n - m;
        long long ans = fact[totalEmpty];
        int prev = -1;
        for (int s : sick) {
            int gap = s - prev - 1;
            if (prev == -1) ans = ans * invFact[gap] % mod;
            else if (gap > 0) ans = ans * invFact[gap] % mod * modPow(2, gap - 1) % mod;
            prev = s;
        }
        int gap = n - prev - 1;
        ans = ans * invFact[gap] % mod;
        return (int)ans;
    }
};
