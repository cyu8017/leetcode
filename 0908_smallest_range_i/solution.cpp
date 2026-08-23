// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int smallestRangeI(std::vector<int>& nums, int k) {
        auto [mn, mx] = std::minmax_element(nums.begin(), nums.end());
        return std::max(0, *mx - *mn - 2 * k);
    }
};
