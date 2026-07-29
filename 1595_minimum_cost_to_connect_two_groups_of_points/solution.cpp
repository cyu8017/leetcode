// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int connectTwoGroups(std::vector<std::vector<int>>& cost) {
        const int m = static_cast<int>(cost.size());
        const int n = static_cast<int>(cost[0].size());
        const int full = 1 << n;
        const int INF = 1000000000;
        std::vector<int> dp(full, INF);
        dp[0] = 0;
        for (const auto& row : cost) {
            std::vector<int> nxt(full, INF);
            for (int mask = 0; mask < full; ++mask) {
                for (int j = 0; j < n; ++j) {
                    const int value = row[j];
                    const int new_mask = mask | (1 << j);
                    nxt[new_mask] = std::min({nxt[new_mask], dp[mask] + value, nxt[mask] + value});
                }
            }
            dp = std::move(nxt);
        }
        std::vector<int> minimum(n, INF);
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                minimum[j] = std::min(minimum[j], cost[i][j]);
            }
        }
        int answer = INF;
        for (int mask = 0; mask < full; ++mask) {
            int extra = 0;
            for (int j = 0; j < n; ++j) {
                if (((mask >> j) & 1) == 0) {
                    extra += minimum[j];
                }
            }
            answer = std::min(answer, dp[mask] + extra);
        }
        return answer;
    }
};
