// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int f = 2, ans = f;
        for (int i = 2; i < (int)nums.size(); i++) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                f++;
                ans = std::max(ans, f);
            } else f = 2;
        }
        return ans;
    }
};
