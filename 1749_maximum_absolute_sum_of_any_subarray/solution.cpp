// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxAbsoluteSum(std::vector<int>& nums) {
        int prefix = 0;
        int low = 0;
        int high = 0;
        for (int value : nums) {
            prefix += value;
            low = std::min(low, prefix);
            high = std::max(high, prefix);
        }
        return high - low;
    }
};
