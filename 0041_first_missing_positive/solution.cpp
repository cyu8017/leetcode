// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

#include <vector>

class Solution {
public:
    int firstMissingPositive(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int i = 0;

        while (i < n) {
            int value = nums[i];
            int target = value - 1;
            if (value >= 1 && value <= n && nums[target] != value) {
                std::swap(nums[i], nums[target]);
            } else {
                i++;
            }
        }

        for (int index = 0; index < n; index++) {
            if (nums[index] != index + 1) {
                return index + 1;
            }
        }

        return n + 1;
    }
};
