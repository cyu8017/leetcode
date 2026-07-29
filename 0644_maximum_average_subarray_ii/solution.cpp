// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

#include <algorithm>
#include <vector>

class Solution {
    bool canReach(const std::vector<int>& nums, int k, double mid) {
        double prefix = 0.0;
        for (int i = 0; i < k; ++i) {
            prefix += nums[i] - mid;
        }
        if (prefix >= 0) {
            return true;
        }
        double prev = 0.0;
        double minPrev = 0.0;
        for (int i = k; i < static_cast<int>(nums.size()); ++i) {
            prefix += nums[i] - mid;
            prev += nums[i - k] - mid;
            minPrev = std::min(minPrev, prev);
            if (prefix - minPrev >= 0) {
                return true;
            }
        }
        return false;
    }

public:
    double findMaxAverage(std::vector<int>& nums, int k) {
        double left = *std::min_element(nums.begin(), nums.end());
        double right = *std::max_element(nums.begin(), nums.end());
        for (int i = 0; i < 80; ++i) {
            const double mid = (left + right) / 2.0;
            if (canReach(nums, k, mid)) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
