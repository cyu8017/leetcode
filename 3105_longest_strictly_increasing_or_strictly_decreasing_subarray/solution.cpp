// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestMonotonicSubarray(std::vector<int>& nums) {
        int ans = 1, t = 1;
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i - 1] < nums[i]) {
                t++;
                ans = std::max(ans, t);
            } else t = 1;
        }
        t = 1;
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i - 1] > nums[i]) {
                t++;
                ans = std::max(ans, t);
            } else t = 1;
        }
        return ans;
    }
};
