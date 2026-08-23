// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> summaryRanges(std::vector<int>& nums) {
        std::vector<std::string> result;
        int index = 0;

        while (index < static_cast<int>(nums.size())) {
            int start = nums[index];
            while (index + 1 < static_cast<int>(nums.size()) && nums[index + 1] == nums[index] + 1) {
                index++;
            }
            if (start == nums[index]) {
                result.push_back(std::to_string(start));
            } else {
                result.push_back(std::to_string(start) + "->" + std::to_string(nums[index]));
            }
            index++;
        }

        return result;
    }
};
