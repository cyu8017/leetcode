// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

#include <stdbool.h>

bool hasAlternatingBits(int n) {
    long long x = n;
    long long y = x ^ (x >> 1);
    return (y & (y + 1)) == 0;
}
