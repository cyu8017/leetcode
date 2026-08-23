// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

#include <algorithm>
#include <cmath>
#include <string>
#include <vector>

class Solution {
public:
    int longestIdealString(std::string s, int k) {
        std::vector<int> dp(26);
        int ans = 0;
        for (char ch : s) {
            int c = ch - 'a';
            int best = 0;
            for (int p = 0; p < 26; p++) {
                if (std::abs(c - p) <= k && dp[p] > best) best = dp[p];
            }
            dp[c] = best + 1;
            ans = std::max(ans, dp[c]);
        }
        return ans;
    }
};
