// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

#include <vector>

class Solution {
public:
    double probabilityOfHeads(std::vector<double>& prob, int target) {
        std::vector<double> dp(target + 1, 0.0);
        dp[0] = 1.0;
        for (double p : prob) {
            for (int heads = target; heads >= 0; --heads) {
                dp[heads] = dp[heads] * (1.0 - p) + (heads ? dp[heads - 1] * p : 0.0);
            }
        }
        return dp[target];
    }
};
