// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

#include <vector>

class Solution {
public:
    int subsetXORSum(std::vector<int>& nums) {
        int bits = 0;
        for (int num : nums) {
            bits |= num;
        }
        int total = 0;
        for (int bit = 1; bit <= bits; bit <<= 1) {
            if (bits & bit) {
                total += bit;
            }
        }
        return total << (static_cast<int>(nums.size()) - 1);
    }
};
