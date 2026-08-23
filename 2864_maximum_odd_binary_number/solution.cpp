// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

#include <string>

class Solution {
public:
    std::string maximumOddBinaryNumber(std::string s) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        int zeros = (int)s.size() - ones;
        std::string b;
        b.reserve(s.size());
        for (int i = 0; i < ones - 1; i++) b.push_back('1');
        for (int i = 0; i < zeros; i++) b.push_back('0');
        b.push_back('1');
        return b;
    }
};
