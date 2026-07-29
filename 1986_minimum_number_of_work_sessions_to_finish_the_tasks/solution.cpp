// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
#include <utility>
#include <vector>

class Solution {
public:
    int minSessions(std::vector<int>& tasks, int sessionTime) {
        int n = (int)tasks.size();
        const std::pair<int, int> INF = {n + 1, 0};
        std::vector<std::pair<int, int>> dp(1 << n, INF);
        dp[0] = {1, 0};
        for (int mask = 0; mask < (1 << n); mask++) {
            auto [sessions, used] = dp[mask];
            if (sessions > n) continue;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int t = tasks[i];
                int nmask = mask | (1 << i);
                std::pair<int, int> cand;
                if (used + t <= sessionTime) cand = {sessions, used + t};
                else cand = {sessions + 1, t};
                if (cand < dp[nmask]) dp[nmask] = cand;
            }
        }
        return dp[(1 << n) - 1].first;
    }
};
