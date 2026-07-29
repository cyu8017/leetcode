// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestSubsequence(std::vector<int>& arr, int difference) {
        std::unordered_map<int, int> dp;
        int best = 0;
        for (int x : arr) {
            dp[x] = dp[x - difference] + 1;
            best = std::max(best, dp[x]);
        }
        return best;
    }
};
