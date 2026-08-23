// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

#include <algorithm>
#include <vector>

class Solution {
    int robLinear(const std::vector<int>& houses) const {
        int previousTwo = 0;
        int previousOne = 0;
        for (int value : houses) {
            const int current = std::max(previousOne, previousTwo + value);
            previousTwo = previousOne;
            previousOne = current;
        }
        return previousOne;
    }

public:
    int rob(std::vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        return std::max(
            robLinear(std::vector<int>(nums.begin(), nums.end() - 1)),
            robLinear(std::vector<int>(nums.begin() + 1, nums.end()))
        );
    }
};
