// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

#include <algorithm>
#include <vector>

class Solution {
    int gcd(int a, int b) {
        if (a == 0) return b;
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }

public:
    int subsequencePairCount(std::vector<int>& nums) {
        const int mod = 1000000007;
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<std::vector<int>> dp(maxV + 1, std::vector<int>(maxV + 1, 0));
        dp[0][0] = 1;
        for (int x : nums) {
            std::vector<std::vector<int>> ndp = dp;
            for (int a = 0; a <= maxV; a++) {
                for (int b = 0; b <= maxV; b++) {
                    if (dp[a][b] == 0) continue;
                    int na = a == 0 ? x : gcd(a, x);
                    int nb = b == 0 ? x : gcd(b, x);
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod;
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod;
                }
            }
            dp = ndp;
        }
        int ans = 0;
        for (int g = 1; g <= maxV; g++) ans = (ans + dp[g][g]) % mod;
        return ans;
    }
};
