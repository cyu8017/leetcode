// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long minimumTime(std::vector<int>& power) {
        int n = (int)power.size();
        int N = 1 << n;
        std::vector<long long> dp(N, LLONG_MAX / 4);
        dp[0] = 0;
        for (int mask = 0; mask < N; mask++) {
            int killed = __builtin_popcount(mask);
            long long gain = killed + 1;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                long long need = (power[i] + gain - 1) / gain;
                int nm = mask | (1 << i);
                dp[nm] = std::min(dp[nm], dp[mask] + need);
            }
        }
        return dp[N - 1];
    }
};
