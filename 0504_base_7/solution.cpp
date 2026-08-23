// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }
        const bool negative = num < 0;
        num = std::abs(num);
        std::string digits;
        while (num > 0) {
            digits.push_back(static_cast<char>('0' + num % 7));
            num /= 7;
        }
        std::reverse(digits.begin(), digits.end());
        if (negative) {
            return "-" + digits;
        }
        return digits;
    }
};
