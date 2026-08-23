// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string smallestNumber(long long n) {
        if (n == 0) return "0";
        if (n == 1) return "1";
        std::string digits;
        for (int d = 9; d >= 2; d--) {
            while (n % d == 0) {
                digits.push_back(char('0' + d));
                n /= d;
            }
        }
        if (n > 1) return "-1";
        std::reverse(digits.begin(), digits.end());
        return digits;
    }
};
