// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> maxActiveSectionsAfterTrade(std::string s, std::vector<std::vector<int>>& queries) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        std::vector<int> ans(queries.size(), ones);
        return ans;
    }
};
