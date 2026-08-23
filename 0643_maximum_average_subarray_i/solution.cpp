// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    double findMaxAverage(std::vector<int>& nums, int k) {
        long long window = 0;
        for (int i = 0; i < k; ++i) {
            window += nums[i];
        }
        long long best = window;
        for (int i = k; i < static_cast<int>(nums.size()); ++i) {
            window += nums[i] - nums[i - k];
            best = std::max(best, window);
        }
        return static_cast<double>(best) / k;
    }
};
