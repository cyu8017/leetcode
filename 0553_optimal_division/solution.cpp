// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

#include <string>
#include <vector>

class Solution {
public:
    std::string optimalDivision(std::vector<int>& nums) {
        if (nums.size() == 1) {
            return std::to_string(nums[0]);
        }
        if (nums.size() == 2) {
            return std::to_string(nums[0]) + "/" + std::to_string(nums[1]);
        }

        std::string result = std::to_string(nums[0]) + "/(";
        for (std::size_t i = 1; i < nums.size(); ++i) {
            if (i > 1) {
                result += '/';
            }
            result += std::to_string(nums[i]);
        }
        result += ')';
        return result;
    }
};
