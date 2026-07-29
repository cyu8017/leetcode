// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

#include <string>

class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        std::string digits = std::to_string(n);
        int mark = static_cast<int>(digits.size());
        for (int i = static_cast<int>(digits.size()) - 1; i > 0; --i) {
            if (digits[i] < digits[i - 1]) {
                digits[i - 1] = static_cast<char>(digits[i - 1] - 1);
                mark = i;
            }
        }
        for (int i = mark; i < static_cast<int>(digits.size()); ++i) {
            digits[i] = '9';
        }
        return std::stoi(digits);
    }
};
