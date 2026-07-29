// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

#include <vector>

class Solution {
public:
    bool canBeIncreasing(std::vector<int>& nums) {
        auto check = [&](int skip) {
            int prev = -1;
            bool hasPrev = false;
            for (int i = 0; i < (int)nums.size(); i++) {
                if (i == skip) continue;
                if (hasPrev && nums[i] <= prev) return false;
                prev = nums[i];
                hasPrev = true;
            }
            return true;
        };
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] <= nums[i - 1]) return check(i - 1) || check(i);
        }
        return true;
    }
};
