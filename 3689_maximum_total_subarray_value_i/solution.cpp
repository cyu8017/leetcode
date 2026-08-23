// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxTotalValue(std::vector<int>& nums, int k) {
        auto [mn, mx] = std::minmax_element(nums.begin(), nums.end());
        return 1LL * k * (*mx - *mn);
    }
};
