// LeetCode 0001 - Two Sum
// https://leetcode.com/problems/two-sum/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.count(complement)) {
                return { seen[complement], i };
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
