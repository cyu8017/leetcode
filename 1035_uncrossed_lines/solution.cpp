// LeetCode 1035 - Uncrossed Lines
// https://leetcode.com/problems/uncrossed-lines/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxUncrossedLines(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = static_cast<int>(nums1.size());
        int n = static_cast<int>(nums2.size());
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (nums1[i - 1] == nums2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m][n];
    }
};

