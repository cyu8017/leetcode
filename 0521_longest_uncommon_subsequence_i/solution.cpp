// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

#include <string>

class Solution {
public:
    int findLUSlength(std::string a, std::string b) {
        return a != b ? static_cast<int>(std::max(a.size(), b.size())) : -1;
    }
};
