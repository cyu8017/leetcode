// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int ops = 0;
        int prev = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] <= prev) {
                int needed = prev + 1;
                ops += needed - nums[i];
                prev = needed;
            } else {
                prev = nums[i];
            }
        }
        return ops;
    }
};
