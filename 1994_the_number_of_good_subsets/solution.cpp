// LeetCode 1994 - The Number of Good Subsets
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;
    long long modPow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
public:
    int numberOfGoodSubsets(std::vector<int>& nums) {
        std::vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        std::vector<int> masks(31, 0);
        for (int x = 2; x <= 30; x++) {
            int m = 0, y = x;
            bool ok = true;
            for (int i = 0; i < (int)primes.size(); i++) {
                int p = primes[i];
                if (y % p == 0) {
                    if ((y / p) % p == 0) { ok = false; break; }
                    m |= 1 << i;
                    y /= p;
                }
            }
            masks[x] = ok ? m : -1;
        }
        std::vector<int> cnt(31, 0);
        for (int v : nums) cnt[v]++;
        int P = (int)primes.size();
        std::vector<long long> dp(1 << P, 0);
        dp[0] = 1;
        for (int x = 2; x <= 30; x++) {
            if (cnt[x] == 0 || masks[x] < 0) continue;
            int m = masks[x];
            for (int state = (1 << P) - 1; state >= 0; state--) {
                if (state & m) continue;
                dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD;
            }
        }
        long long ans = 0;
        for (int i = 1; i < (1 << P); i++) ans = (ans + dp[i]) % MOD;
        ans = ans * modPow(2, cnt[1]) % MOD;
        return (int)ans;
    }
};
