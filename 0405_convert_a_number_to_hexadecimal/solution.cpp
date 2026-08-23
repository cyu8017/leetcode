// LeetCode 0405 - Convert a Number to Hexadecimal
// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

#include <algorithm>
#include <string>

class Solution {
public:
    string toHex(int num) {
        if (num == 0) {
            return "0";
        }

        const char* digits = "0123456789abcdef";
        unsigned int value = static_cast<unsigned int>(num);
        string result;

        while (value) {
            result.push_back(digits[value & 15]);
            value >>= 4;
        }

        reverse(result.begin(), result.end());
        return result;
    }
};
