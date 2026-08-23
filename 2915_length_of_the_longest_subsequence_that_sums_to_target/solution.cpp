// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

#include <vector>

class Solution {
public:
    int lengthOfLongestSubsequence(std::vector<int>& nums, int target) {
        std::vector<int> dp(target + 1, -1);
        dp[0] = 0;
        for (int v : nums)
            for (int s = target; s >= v; s--)
                if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1;
        return dp[target];
    }
};
