// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

#include <map>
#include <string>
#include <utility>
#include <vector>

class Solution {
    static int modPow(long long a, long long e, int mod) {
        long long r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int)r;
    }

public:
    int countBalancedPermutations(std::string num) {
        const int mod = 1000000007;
        int cnt[10] = {};
        int sum = 0;
        for (char c : num) {
            cnt[c - '0']++;
            sum += c - '0';
        }
        if (sum % 2 == 1) return 0;
        int n = (int)num.size();
        int halfN = n / 2, halfS = sum / 2;
        std::vector<int> fact(n + 1), invF(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = (int)((long long)fact[i - 1] * i % mod);
        invF[n] = modPow(fact[n], mod - 2, mod);
        for (int i = n; i > 0; i--) invF[i - 1] = (int)((long long)invF[i] * i % mod);

        std::map<std::pair<int, int>, int> dp;
        dp[{0, 0}] = 1;
        for (int d = 0; d <= 9; d++) {
            std::map<std::pair<int, int>, int> ndp;
            for (auto& [st, ways] : dp) {
                int used = st.first, s = st.second;
                for (int take = 0; take <= cnt[d]; take++) {
                    int nu = used + take, ns = s + take * d;
                    if (nu > halfN || ns > halfS) continue;
                    int w = (int)((long long)ways * invF[take] % mod * invF[cnt[d] - take] % mod);
                    ndp[{nu, ns}] = (ndp[{nu, ns}] + w) % mod;
                }
            }
            dp.swap(ndp);
        }
        int ans = dp[{halfN, halfS}];
        ans = (int)((long long)ans * fact[halfN] % mod * fact[n - halfN] % mod);
        for (int d = 0; d <= 9; d++) ans = (int)((long long)ans * fact[cnt[d]] % mod);
        return ans;
    }
};
