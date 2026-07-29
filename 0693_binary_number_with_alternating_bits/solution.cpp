// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
public:
    bool hasAlternatingBits(int n) {
        const unsigned x = static_cast<unsigned>(n) ^ (static_cast<unsigned>(n) >> 1);
        return (x & (x + 1)) == 0;
    }
};
