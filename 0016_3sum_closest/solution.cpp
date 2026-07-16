// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int threeSumClosest(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < static_cast<int>(nums.size()) - 2; i++) {
            int left = i + 1;
            int right = static_cast<int>(nums.size()) - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (std::abs(total - target) < std::abs(closest - target)) {
                    closest = total;
                }
                if (total < target) {
                    left++;
                } else if (total > target) {
                    right--;
                } else {
                    return total;
                }
            }
        }

        return closest;
    }
};
