// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxAscendingSum(std::vector<int>& nums) {
        int best = nums[0];
        int cur = nums[0];
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] > nums[i - 1]) {
                cur += nums[i];
            } else {
                cur = nums[i];
            }
            best = std::max(best, cur);
        }
        return best;
    }
};
