// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

#include <vector>
#include <algorithm>
#include <cstdint>

class Solution {
public:
    long long maxCoins(std::vector<int>& lane1, std::vector<int>& lane2) {
        int n = (int)lane1.size();
        const long long neg = (long long)(-1LL << 60);
        long long dp[2][2];
        dp[0][0] = lane1[0];
        dp[1][0] = lane2[0];
        dp[0][1] = dp[1][1] = neg;
        long long ans = std::max(dp[0][0], dp[1][0]);
        for (int i = 1; i < n; i++) {
            long long ndp[2][2];
            ndp[0][0] = std::max(dp[0][0], 0LL) + lane1[i];
            ndp[1][0] = std::max(dp[1][0], 0LL) + lane2[i];
            ndp[0][1] = std::max(dp[0][1], dp[1][0]) + lane1[i];
            ndp[1][1] = std::max(dp[1][1], dp[0][0]) + lane2[i];
            if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i];
            if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i];
            for (int a = 0; a < 2; a++)
                for (int b = 0; b < 2; b++) {
                    dp[a][b] = ndp[a][b];
                    if (dp[a][b] > ans) ans = dp[a][b];
                }
        }
        return ans;
    }
};
