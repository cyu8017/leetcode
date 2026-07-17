// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

#include <string>

class Solution {
public:
    std::string maximumBinaryString(std::string binary) {
        int zeros = 0;
        for (char ch : binary) {
            if (ch == '0') {
                zeros++;
            }
        }
        if (zeros <= 1) {
            return binary;
        }
        int first = static_cast<int>(binary.find('0'));
        int n = static_cast<int>(binary.size());
        return std::string(first + zeros - 1, '1') + "0" + std::string(n - first - zeros, '1');
    }
};
