// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

#include <cmath>
#include <string>

class Solution {
    long long buildPalindrome(int value) {
        const std::string text = std::to_string(value);
        const std::string reversed(text.rbegin(), text.rend());
        return std::stoll(text + reversed);
    }

public:
    int largestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }
        const int upper = static_cast<int>(std::pow(10, n)) - 1;
        const int lower = static_cast<int>(std::pow(10, n - 1));
        for (int first = upper; first >= lower; --first) {
            const long long candidate = buildPalindrome(first);
            for (int factor = upper; static_cast<long long>(factor) * factor >= candidate; --factor) {
                if (candidate % factor == 0) {
                    const long long partner = candidate / factor;
                    if (partner >= lower && partner <= upper) {
                        return static_cast<int>(candidate % 1337);
                    }
                }
            }
        }
        return 0;
    }
};
