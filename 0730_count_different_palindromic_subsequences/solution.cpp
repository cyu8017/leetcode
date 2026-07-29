// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

#include <string>
#include <vector>

class Solution {
public:
    int countPalindromicSubsequences(std::string s) {
        const int mod = 1000000007;
        int n = static_cast<int>(s.size());
        std::vector<std::vector<long long>> dp(n, std::vector<long long>(n, 0));
        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i <= n - length; ++i) {
                int j = i + length - 1;
                if (s[i] != s[j]) {
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1];
                } else {
                    int left = i + 1;
                    int right = j - 1;
                    while (left <= right && s[left] != s[i]) {
                        ++left;
                    }
                    while (left <= right && s[right] != s[i]) {
                        --right;
                    }
                    if (left > right) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                    } else if (left == right) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1];
                    }
                }
                dp[i][j] = (dp[i][j] % mod + mod) % mod;
            }
        }
        return static_cast<int>(dp[0][n - 1]);
    }
};
