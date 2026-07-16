// LeetCode 0371 - Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

class Solution {
public:
    int getSum(int a, int b) {
        unsigned int mask = 0xFFFFFFFFu;

        while (b) {
            unsigned int carry = static_cast<unsigned int>(a & b) << 1;
            a = (a ^ b) & static_cast<int>(mask);
            b = static_cast<int>(carry & mask);
        }

        return a <= 0x7FFFFFFF ? a : static_cast<int>(~(a ^ mask));
    }
};
