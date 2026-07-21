// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

#include <vector>

class Solution {
public:
    int getXORSum(std::vector<int>& arr1, std::vector<int>& arr2) {
        int xor1 = 0;
        for (int value : arr1) {
            xor1 ^= value;
        }
        int xor2 = 0;
        for (int value : arr2) {
            xor2 ^= value;
        }
        return xor1 & xor2;
    }
};
