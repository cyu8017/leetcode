// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

#include <vector>

class Solution {
public:
    std::vector<int> evenOddBit(int n) {
        int even = 0, odd = 0, i = 0;
        while (n > 0) {
            if (n & 1) {
                if (i % 2 == 0) even++;
                else odd++;
            }
            n >>= 1;
            i++;
        }
        return {even, odd};
    }
};
