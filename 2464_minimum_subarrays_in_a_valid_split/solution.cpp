// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

#include <numeric>
#include <vector>

class Solution {
public:
    int validSubarraySplit(std::vector<int>& nums) {
        int n = (int)nums.size();
        const int INF = 1 << 30;
        std::vector<int> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] >= INF) continue;
            for (int j = i; j < n; j++) {
                if (std::gcd(nums[i], nums[j]) > 1) {
                    if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
                }
            }
        }
        return dp[n] >= INF ? -1 : dp[n];
    }
};
