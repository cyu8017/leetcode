// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximizeSum(std::vector<int>& nums, int k) {
        int mx = *std::max_element(nums.begin(), nums.end());
        return k * mx + k * (k - 1) / 2;
    }
};
