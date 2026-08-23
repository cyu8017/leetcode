// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, std::vector<int>& target) {
        std::unordered_set<int> s;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] != target[i]) s.insert(nums[i]);
        }
        return (int)s.size();
    }
};
