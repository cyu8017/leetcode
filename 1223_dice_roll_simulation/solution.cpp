// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

#include <numeric>
#include <vector>

class Solution {
public:
    int dieSimulator(int n, std::vector<int>& rollMax) {
        const int mod = 1000000007;
        std::vector<std::vector<long long>> dp(6);
        for (int j = 0; j < 6; ++j) {
            dp[j].assign(rollMax[j] + 1, 0);
            dp[j][1] = 1;
        }
        for (int step = 1; step < n; ++step) {
            std::vector<long long> totals(6);
            for (int j = 0; j < 6; ++j) {
                totals[j] = std::accumulate(dp[j].begin(), dp[j].end(), 0LL) % mod;
            }
            long long all = std::accumulate(totals.begin(), totals.end(), 0LL) % mod;
            std::vector<std::vector<long long>> nxt(6);
            for (int j = 0; j < 6; ++j) {
                nxt[j].assign(dp[j].size(), 0);
                nxt[j][1] = (all - totals[j] + mod) % mod;
                for (int run = 2; run < static_cast<int>(dp[j].size()); ++run) {
                    nxt[j][run] = dp[j][run - 1];
                }
            }
            dp.swap(nxt);
        }
        long long answer = 0;
        for (const auto& row : dp) {
            for (long long x : row) {
                answer = (answer + x) % mod;
            }
        }
        return static_cast<int>(answer);
    }
};
