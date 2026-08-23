// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findLengthOfLCIS(std::vector<int>& nums) {
        int best = 1;
        int cur = 1;
        for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
            if (nums[i] > nums[i - 1]) {
                ++cur;
                best = std::max(best, cur);
            } else {
                cur = 1;
            }
        }
        return best;
    }
};
