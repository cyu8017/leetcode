// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int smallestRangeII(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = nums.back() - nums.front();
        for (int i = 0; i + 1 < (int)nums.size(); i++) {
            int lo = std::min(nums.front() + k, nums[i + 1] - k);
            int hi = std::max(nums.back() - k, nums[i] + k);
            ans = std::min(ans, hi - lo);
        }
        return ans;
    }
};
