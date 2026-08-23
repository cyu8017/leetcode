// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int mx = *std::max_element(nums.begin(), nums.end());
        int ans = 0, cur = 0;
        for (int x : nums) {
            if (x == mx) {
                cur++;
                ans = std::max(ans, cur);
            } else {
                cur = 0;
            }
        }
        return ans;
    }
};
