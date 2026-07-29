// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

#include <string>

class Solution {
public:
    std::string largestOddNumber(std::string num) {
        for (int i = (int)num.size() - 1; i >= 0; i--) {
            if ((num[i] - '0') % 2) return num.substr(0, i + 1);
        }
        return "";
    }
};
