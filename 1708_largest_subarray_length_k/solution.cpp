// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

#include <vector>

class Solution {
public:
    std::vector<int> largestSubarray(std::vector<int>& nums, int k) {
        int start = 0;
        for (int i = 1; i + k <= static_cast<int>(nums.size()); i++) {
            if (nums[i] > nums[start]) {
                start = i;
            }
        }
        return std::vector<int>(nums.begin() + start, nums.begin() + start + k);
    }
};
