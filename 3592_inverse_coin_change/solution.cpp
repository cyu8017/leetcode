// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

#include <vector>

class Solution {
public:
    std::vector<int> findCoins(std::vector<int>& numWays) {
        int n = (int)numWays.size();
        std::vector<int> dp(n + 1), coins;
        dp[0] = 1;
        for (int amt = 1; amt <= n; amt++) {
            int ways = numWays[amt - 1];
            if (dp[amt] == ways) continue;
            if (dp[amt] + 1 == ways) {
                coins.push_back(amt);
                for (int x = amt; x <= n; x++) dp[x] += dp[x - amt];
                if (dp[amt] != ways) return {};
                continue;
            }
            return {};
        }
        return coins;
    }
};
