// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

#include <algorithm>
#include <vector>

class Solution {
public:
    int profitableSchemes(int n, int minProfit, std::vector<int>& group,
                          std::vector<int>& profit) {
        const int MOD = 1'000'000'007;
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(minProfit + 1, 0));
        dp[0][0] = 1;
        for (size_t i = 0; i < group.size(); ++i) {
            int members = group[i], p = profit[i];
            for (int people = n; people >= members; --people) {
                for (int prof = minProfit; prof >= 0; --prof) {
                    int np = std::min(minProfit, prof + p);
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD;
                }
            }
        }
        int ans = 0;
        for (int people = 0; people <= n; ++people) {
            ans = (ans + dp[people][minProfit]) % MOD;
        }
        return ans;
    }
};
