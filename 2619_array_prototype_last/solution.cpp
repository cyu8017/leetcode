// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    int last(std::vector<int>& nums) {
        if (nums.empty()) return -1;
        return nums.back();
    }
};
