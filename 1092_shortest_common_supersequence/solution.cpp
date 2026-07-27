// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string shortestCommonSupersequence(std::string str1, std::string str2) {
        int m = static_cast<int>(str1.size());
        int n = static_cast<int>(str2.size());
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        int i = m;
        int j = n;
        std::string chars;
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                chars.push_back(str1[i - 1]);
                --i;
                --j;
            } else if (dp[i - 1][j] >= dp[i][j - 1]) {
                chars.push_back(str1[i - 1]);
                --i;
            } else {
                chars.push_back(str2[j - 1]);
                --j;
            }
        }
        while (i > 0) {
            chars.push_back(str1[--i]);
        }
        while (j > 0) {
            chars.push_back(str2[--j]);
        }
        std::reverse(chars.begin(), chars.end());
        return chars;
    }
};
