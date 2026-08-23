// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

#include <vector>

class Solution {
public:
    int upperBound(std::vector<int>& nums, int target) {
        int lo = 0, hi = (int)nums.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
};
