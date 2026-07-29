// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool isMajorityElement(std::vector<int>& nums, int target) {
        auto left = std::lower_bound(nums.begin(), nums.end(), target);
        auto right = std::upper_bound(nums.begin(), nums.end(), target);
        return (right - left) > static_cast<int>(nums.size()) / 2;
    }
};
