// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

#include <string>

class Solution {
public:
    bool repeatedSubstringPattern(std::string s) {
        const std::string doubled = s + s;
        const std::string inner = doubled.substr(1, doubled.size() - 2);
        return inner.find(s) != std::string::npos;
    }
};
