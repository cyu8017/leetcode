// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

#include <stdbool.h>

bool checkZeroOnes(char* s) {
    int maxZeros = 0, maxOnes = 0, zeros = 0, ones = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '0') {
            zeros++;
            ones = 0;
            if (zeros > maxZeros) maxZeros = zeros;
        } else {
            ones++;
            zeros = 0;
            if (ones > maxOnes) maxOnes = ones;
        }
    }
    return maxOnes > maxZeros;
}
