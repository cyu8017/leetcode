// LeetCode 0375 - Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

#include <climits>
#include <vector>

class Solution {
public:
    int getMoneyAmount(int n) {
        std::vector<std::vector<int>> dp(n + 2, std::vector<int>(n + 2, 0));

        for (int length = 2; length <= n; ++length) {
            for (int left = 1; left <= n - length + 1; ++left) {
                int right = left + length - 1;
                dp[left][right] = INT_MAX;
                for (int guess = left; guess < right; ++guess) {
                    int cost = guess + std::max(dp[left][guess - 1], dp[guess + 1][right]);
                    dp[left][right] = std::min(dp[left][right], cost);
                }
            }
        }

        return dp[1][n];
    }
};
