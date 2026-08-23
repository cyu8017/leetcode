// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

#include <vector>

class Solution {
public:
    bool hasIncreasingSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        auto inc = [&](int start) {
            for (int i = start; i + 1 < start + k; i++) {
                if (nums[i] >= nums[i + 1]) return false;
            }
            return true;
        };
        for (int i = 0; i + 2 * k <= n; i++) {
            if (inc(i) && inc(i + k)) return true;
        }
        return false;
    }
};
