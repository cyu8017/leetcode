// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int squareFreeSubsets(std::vector<int>& nums) {
        const int MOD = 1000000007;
        std::vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        auto maskOf = [&](int x) {
            int mask = 0;
            for (int i = 0; i < (int)primes.size(); ++i) {
                int p = primes[i], cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    cnt++;
                    if (cnt > 1) return -1;
                }
                if (cnt == 1) mask |= 1 << i;
            }
            return mask;
        };
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        std::vector<int> dp(1 << 10);
        dp[0] = 1;
        for (auto& [x, c] : freq) {
            if (x == 1) continue;
            int m = maskOf(x);
            if (m < 0) continue;
            for (int state = (1 << 10) - 1; state >= 0; --state) {
                if ((state & m) == 0) {
                    dp[state | m] = (dp[state | m] + (long long)dp[state] * c) % MOD;
                }
            }
        }
        int ans = 0;
        for (int v : dp) ans = (ans + v) % MOD;
        int ones = freq[1];
        int mul = 1;
        for (int i = 0; i < ones; ++i) mul = mul * 2 % MOD;
        ans = (long long)ans * mul % MOD;
        ans = (ans - 1 + MOD) % MOD;
        return ans;
    }
};
