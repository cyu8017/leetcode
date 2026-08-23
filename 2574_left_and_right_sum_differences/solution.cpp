// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> leftRightDifference(std::vector<int>& nums) {
        int total = 0;
        for (int x : nums) total += x;
        std::vector<int> ans(nums.size());
        int left = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int right = total - left - nums[i];
            ans[i] = std::abs(left - right);
            left += nums[i];
        }
        return ans;
    }
};
