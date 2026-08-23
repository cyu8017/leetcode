// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

#include <vector>

class Solution {
public:
    int waysToReachTarget(int target, std::vector<std::vector<int>>& types) {
        const int MOD = 1000000007;
        std::vector<int> dp(target + 1);
        dp[0] = 1;
        for (auto& t : types) {
            int count = t[0], marks = t[1];
            for (int s = target; s >= 0; --s) {
                for (int k = 1; k <= count && s - k * marks >= 0; ++k) {
                    dp[s] = (dp[s] + dp[s - k * marks]) % MOD;
                }
            }
        }
        return dp[target];
    }
};
