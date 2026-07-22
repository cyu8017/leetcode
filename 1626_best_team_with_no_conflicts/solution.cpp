// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
public:
    int bestTeamScore(std::vector<int>& scores, std::vector<int>& ages) {
        const int n = static_cast<int>(scores.size());
        std::vector<std::pair<int, int>> players;
        players.reserve(n);
        for (int i = 0; i < n; ++i) {
            players.push_back({ages[i], scores[i]});
        }
        std::sort(players.begin(), players.end());
        std::vector<int> dp(n, 0);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            const int score = players[i].second;
            dp[i] = score;
            for (int j = 0; j < i; ++j) {
                if (players[j].second <= score) {
                    dp[i] = std::max(dp[i], dp[j] + score);
                }
            }
            ans = std::max(ans, dp[i]);
        }
        return ans;
    }
};
