// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        int m = static_cast<int>(text1.size()), n = static_cast<int>(text2.size());
        std::vector<int> dp(n + 1, 0);
        for (int i = 1; i <= m; ++i) {
            int prev = 0;
            for (int j = 1; j <= n; ++j) {
                int cur = dp[j];
                if (text1[i - 1] == text2[j - 1]) dp[j] = prev + 1;
                else dp[j] = std::max(dp[j], dp[j - 1]);
                prev = cur;
            }
        }
        return dp[n];
    }
};
