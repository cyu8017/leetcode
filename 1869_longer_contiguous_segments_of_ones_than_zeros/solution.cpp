// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

#include <algorithm>
#include <string>

class Solution {
public:
    bool checkZeroOnes(std::string s) {
        int maxZeros = 0;
        int maxOnes = 0;
        int zeros = 0;
        int ones = 0;
        for (char ch : s) {
            if (ch == '0') {
                zeros++;
                ones = 0;
                maxZeros = std::max(maxZeros, zeros);
            } else {
                ones++;
                zeros = 0;
                maxOnes = std::max(maxOnes, ones);
            }
        }
        return maxOnes > maxZeros;
    }
};
