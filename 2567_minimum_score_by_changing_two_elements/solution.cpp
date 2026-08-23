// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimizeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        int a = nums[n - 1] - nums[2];
        int b = nums[n - 3] - nums[0];
        int c = nums[n - 2] - nums[1];
        return std::min({a, b, c});
    }
};
