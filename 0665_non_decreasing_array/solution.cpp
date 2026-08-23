// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

#include <vector>

class Solution {
public:
    bool checkPossibility(std::vector<int>& nums) {
        bool changed = false;
        for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
            if (nums[i] >= nums[i - 1]) {
                continue;
            }
            if (changed) {
                return false;
            }
            changed = true;
            if (i >= 2 && nums[i] < nums[i - 2]) {
                nums[i] = nums[i - 1];
            } else {
                nums[i - 1] = nums[i];
            }
        }
        return true;
    }
};
