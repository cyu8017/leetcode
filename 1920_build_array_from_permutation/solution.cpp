// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

#include <vector>

class Solution {
public:
    std::vector<int> buildArray(std::vector<int>& nums) {
        std::vector<int> res(nums.size());
        for (int i = 0; i < (int)nums.size(); i++) res[i] = nums[nums[i]];
        return res;
    }
};
