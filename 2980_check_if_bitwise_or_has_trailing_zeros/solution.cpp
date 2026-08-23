// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

#include <vector>

class Solution {
public:
    bool hasTrailingZeros(std::vector<int>& nums) {
        int even = 0;
        for (int v : nums) {
            if (v % 2 == 0) {
                even++;
                if (even >= 2) return true;
            }
        }
        return false;
    }
};
