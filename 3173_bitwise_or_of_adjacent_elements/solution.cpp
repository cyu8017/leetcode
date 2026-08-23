// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

#include <vector>

class Solution {
public:
    std::vector<int> orArray(std::vector<int>& nums) {
        std::vector<int> ans;
        for (int i = 1; i < (int)nums.size(); i++) ans.push_back(nums[i] | nums[i - 1]);
        return ans;
    }
};
