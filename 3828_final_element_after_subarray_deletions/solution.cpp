// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

#include <algorithm>
#include <vector>

class Solution {
public:
    int finalElement(std::vector<int>& nums) {
        return std::max(nums.front(), nums.back());
    }
};
