// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

#include <algorithm>
#include <climits>
#include <string>

class Solution {
public:
    int nextGreaterElement(int n) {
        std::string digits = std::to_string(n);
        int i = static_cast<int>(digits.size()) - 2;
        while (i >= 0 && digits[i] >= digits[i + 1]) {
            --i;
        }
        if (i < 0) {
            return -1;
        }

        int j = static_cast<int>(digits.size()) - 1;
        while (digits[j] <= digits[i]) {
            --j;
        }
        std::swap(digits[i], digits[j]);
        std::reverse(digits.begin() + i + 1, digits.end());

        long long value = 0;
        for (char ch : digits) {
            value = value * 10 + (ch - '0');
        }
        if (value > INT_MAX) {
            return -1;
        }
        return static_cast<int>(value);
    }
};
