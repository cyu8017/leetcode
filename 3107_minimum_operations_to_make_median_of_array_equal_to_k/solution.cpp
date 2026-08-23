// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minOperationsToMakeMedianK(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size(), m = n >> 1;
        long long ans = std::abs(nums[m] - k);
        if (nums[m] > k) {
            for (int i = m - 1; i >= 0 && nums[i] > k; i--) ans += nums[i] - k;
        } else {
            for (int i = m + 1; i < n && nums[i] < k; i++) ans += k - nums[i];
        }
        return ans;
    }
};
