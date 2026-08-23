// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

#include <string>

class Solution {
public:
    std::string largestEven(std::string s) {
        while (!s.empty() && s.back() == '1') s.pop_back();
        return s;
    }
};
