// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

#include <algorithm>
#include <cmath>
#include <string>

class Solution {
public:
    int minSwaps(std::string s) {
        int zeros = static_cast<int>(std::count(s.begin(), s.end(), '0'));
        int ones = static_cast<int>(s.size()) - zeros;
        if (std::abs(zeros - ones) > 1) {
            return -1;
        }

        auto mismatches = [&](char first) {
            int count = 0;
            for (int i = 0; i < static_cast<int>(s.size()); i++) {
                char expected = (i % 2 == 0) ? first : (first == '0' ? '1' : '0');
                if (s[i] != expected) count++;
            }
            return count / 2;
        };

        if (zeros == ones) {
            return std::min(mismatches('0'), mismatches('1'));
        }
        if (zeros > ones) {
            return mismatches('0');
        }
        return mismatches('1');
    }
};
