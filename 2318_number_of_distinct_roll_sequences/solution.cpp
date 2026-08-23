// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

#include <vector>
#include <numeric>

class Solution {
public:
    int distinctSequences(int n) {
        const int mod = 1000000007;
        auto gcd = [](int a, int b) {
            while (b) { int t = a % b; a = b; b = t; }
            return a;
        };
        std::vector<std::vector<std::vector<int>>> dp(n + 1, std::vector<std::vector<int>>(7, std::vector<int>(7)));
        for (int a = 1; a <= 6; ++a) dp[1][a][0] = 1;
        for (int i = 2; i <= n; ++i) {
            for (int prev = 1; prev <= 6; ++prev) {
                for (int pprev = 0; pprev <= 6; ++pprev) {
                    if (!dp[i - 1][prev][pprev]) continue;
                    for (int cur = 1; cur <= 6; ++cur) {
                        if (cur == prev || cur == pprev || gcd(cur, prev) != 1) continue;
                        dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod;
                    }
                }
            }
        }
        int ans = 0;
        for (int a = 1; a <= 6; ++a)
            for (int b = 0; b <= 6; ++b)
                ans = (ans + dp[n][a][b]) % mod;
        return ans;
    }
};
