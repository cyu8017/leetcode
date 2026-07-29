// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

#include <vector>

class Solution {
public:
    int numSubarrayBoundedMax(std::vector<int>& nums, int left, int right) {
        return countAtMost(nums, right) - countAtMost(nums, left - 1);
    }

private:
    int countAtMost(const std::vector<int>& nums, int bound) {
        int ans = 0;
        int cur = 0;
        for (int num : nums) {
            if (num <= bound) {
                ++cur;
                ans += cur;
            } else {
                cur = 0;
            }
        }
        return ans;
    }
};
