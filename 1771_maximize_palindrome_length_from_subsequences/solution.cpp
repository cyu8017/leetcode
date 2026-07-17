// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int longestPalindrome(std::string word1, std::string word2) {
        std::string s = word1 + word2;
        int n = (int)s.size();
        int n1 = (int)word1.size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        int ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    dp[i][j] = (j == i + 1) ? 2 : dp[i + 1][j - 1] + 2;
                    if (i < n1 && n1 <= j) {
                        ans = std::max(ans, dp[i][j]);
                    }
                } else {
                    dp[i][j] = std::max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return ans;
    }
};
