// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int maximumJumps(std::vector<int>& nums, int target) {
        int n = (int)nums.size();
        std::vector<int> dp(n, -1);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] < 0) continue;
            for (int j = i + 1; j < n; j++) {
                if (std::abs(nums[j] - nums[i]) <= target) {
                    dp[j] = std::max(dp[j], dp[i] + 1);
                }
            }
        }
        return dp[n - 1];
    }
};
