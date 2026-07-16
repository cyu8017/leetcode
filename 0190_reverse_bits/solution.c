// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

#include <stdint.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    for (int bit = 0; bit < 32; ++bit) {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    return result;
}