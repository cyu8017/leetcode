// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

#include <algorithm>
#include <vector>

class Solution {
public:
    int twoSumLessThanK(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int lo = 0;
        int hi = static_cast<int>(nums.size()) - 1;
        int ans = -1;
        while (lo < hi) {
            int total = nums[lo] + nums[hi];
            if (total < k) {
                ans = std::max(ans, total);
                ++lo;
            } else {
                --hi;
            }
        }
        return ans;
    }
};
