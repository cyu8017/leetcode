// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

#include <vector>

class Solution {
public:
    long long zeroFilledSubarray(std::vector<int>& nums) {
        long long ans = 0, streak = 0;
        for (int x : nums) {
            if (x == 0) {
                streak++;
                ans += streak;
            } else {
                streak = 0;
            }
        }
        return ans;
    }
};
