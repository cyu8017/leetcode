// LeetCode 0191 - Number of 1 Bits
// https://leetcode.com/problems/number-of-1-bits/

#include <stdint.h>

int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) {
        n &= n - 1;
        ++count;
    }
    return count;
}
