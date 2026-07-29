// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int maxSubarraySumCircular(std::vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int maxSum = nums[0], minSum = nums[0], curMax = nums[0], curMin = nums[0];
        for (int i = 1; i < (int)nums.size(); i++) {
            curMax = std::max(nums[i], curMax + nums[i]);
            curMin = std::min(nums[i], curMin + nums[i]);
            maxSum = std::max(maxSum, curMax);
            minSum = std::min(minSum, curMin);
        }
        if (maxSum < 0) return maxSum;
        return std::max(maxSum, total - minSum);
    }
};
