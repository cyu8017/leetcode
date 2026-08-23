// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

#include <vector>

class Solution {
public:
    int evenNumberBitwiseORs(std::vector<int>& nums) {
        int ans = 0;
        for (int x : nums) if (x % 2 == 0) ans |= x;
        return ans;
    }
};
