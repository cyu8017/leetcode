// LeetCode 0377 - Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

#include <vector>

class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) {
        std::vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;

        for (int amount = 1; amount <= target; ++amount) {
            for (int num : nums) {
                if (amount >= num) {
                    dp[amount] += dp[amount - num];
                }
            }
        }

        return static_cast<int>(dp[target]);
    }
};
