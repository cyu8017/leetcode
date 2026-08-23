// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

#include <cstdlib>
#include <numeric>
#include <vector>

class Solution {
public:
    int findTargetSumWays(std::vector<int>& nums, int target) {
        const long long total = std::accumulate(nums.begin(), nums.end(), 0LL);
        if ((total + target) % 2 != 0 || std::llabs(target) > total) {
            return 0;
        }
        const int need = static_cast<int>((total + target) / 2);
        std::vector<int> dp(need + 1, 0);
        dp[0] = 1;
        for (int num : nums) {
            for (int amount = need; amount >= num; --amount) {
                dp[amount] += dp[amount - num];
            }
        }
        return dp[need];
    }
};
