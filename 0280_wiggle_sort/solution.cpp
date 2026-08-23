// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

#include <vector>

class Solution {
public:
    void wiggleSort(std::vector<int>& nums) {
        for (int index = 1; index < static_cast<int>(nums.size()); index++) {
            if (index % 2 == 1 && nums[index] < nums[index - 1]) {
                std::swap(nums[index], nums[index - 1]);
            } else if (index % 2 == 0 && nums[index] > nums[index - 1]) {
                std::swap(nums[index], nums[index - 1]);
            }
        }
    }
};
