// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> getLongestSubsequence(std::vector<std::string>& words, std::vector<int>& groups) {
        std::vector<std::string> ans = {words[0]};
        int last = groups[0];
        for (int i = 1; i < (int)words.size(); i++) {
            if (groups[i] != last) {
                ans.push_back(words[i]);
                last = groups[i];
            }
        }
        return ans;
    }
};
