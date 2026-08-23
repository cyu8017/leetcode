// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        for (int x : nums) if (x != nums[0]) return 1;
        return 0;
    }
};
