// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minimumTotalDistance(std::vector<int>& robot, std::vector<std::vector<int>>& factory) {
        std::sort(robot.begin(), robot.end());
        std::sort(factory.begin(), factory.end());
        int m = (int)robot.size();
        std::vector<int> pos;
        for (auto& f : factory) {
            for (int c = 0; c < f[1]; c++) pos.push_back(f[0]);
        }
        int n = (int)pos.size();
        const long long INF = 1LL << 60;
        std::vector<std::vector<long long>> dp(m + 1, std::vector<long long>(n + 1, INF));
        for (int j = 0; j <= n; j++) dp[0][j] = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = i; j <= n; j++) {
                dp[i][j] = dp[i][j - 1];
                long long diff = robot[i - 1] - pos[j - 1];
                if (diff < 0) diff = -diff;
                if (dp[i - 1][j - 1] + diff < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + diff;
            }
        }
        return dp[m][n];
    }
};
