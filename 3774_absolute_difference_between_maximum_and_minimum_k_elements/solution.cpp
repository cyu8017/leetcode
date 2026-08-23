// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    int absDifference(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 0, n = (int)nums.size();
        for (int i = 0; i < k; i++) ans += nums[n - i - 1] - nums[i];
        return ans;
    }
};
