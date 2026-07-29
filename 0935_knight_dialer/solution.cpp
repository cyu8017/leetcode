// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

#include <vector>

class Solution {
public:
    int knightDialer(int n) {
        const int MOD = 1000000007;
        std::vector<std::vector<int>> moves = {
            {4,6},{6,8},{7,9},{4,8},{0,3,9},{},{0,1,7},{2,6},{1,3},{2,4}
        };
        std::vector<long long> dp(10, 1);
        for (int step = 0; step < n - 1; step++) {
            std::vector<long long> ndp(10, 0);
            for (int i = 0; i < 10; i++)
                for (int j : moves[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
            dp.swap(ndp);
        }
        long long ans = 0;
        for (auto x : dp) ans = (ans + x) % MOD;
        return (int)ans;
    }
};
