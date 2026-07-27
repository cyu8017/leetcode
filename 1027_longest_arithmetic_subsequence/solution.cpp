// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestArithSeqLength(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        std::vector<std::unordered_map<int, int>> dp(n);
        int ans = 1;
        for (int j = 1; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                int d = nums[j] - nums[i];
                int prev = dp[i].count(d) ? dp[i][d] : 1;
                dp[j][d] = prev + 1;
                ans = std::max(ans, dp[j][d]);
            }
        }
        return ans;
    }
};

