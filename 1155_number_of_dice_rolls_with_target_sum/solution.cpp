// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

#include <vector>

class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        const int MOD = 1e9 + 7;
        std::vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (int dice = 0; dice < n; ++dice) {
            std::vector<int> neu(target + 1, 0);
            for (int s = 0; s <= target; ++s) {
                if (!dp[s]) continue;
                for (int face = 1; face <= k; ++face) {
                    if (s + face <= target) neu[s + face] = (neu[s + face] + dp[s]) % MOD;
                }
            }
            dp.swap(neu);
        }
        return dp[target];
    }
};
