// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

#include <algorithm>
#include <limits>
#include <vector>

class Solution {
public:
    int minSideJumps(std::vector<int>& obstacles) {
        const int INF = std::numeric_limits<int>::max() / 4;
        std::vector<int> dp = {1, 0, 1};
        for (int obs : obstacles) {
            std::vector<char> blocked = {
                static_cast<char>(obs == 1),
                static_cast<char>(obs == 2),
                static_cast<char>(obs == 3),
            };
            std::vector<int> ndp = {INF, INF, INF};
            for (int lane = 0; lane < 3; ++lane) {
                if (blocked[lane]) {
                    continue;
                }
                for (int other = 0; other < 3; ++other) {
                    if (blocked[other] || dp[other] == INF) {
                        continue;
                    }
                    ndp[lane] = std::min(ndp[lane], dp[other] + (lane != other));
                }
            }
            dp = std::move(ndp);
        }
        return *std::min_element(dp.begin(), dp.end());
    }
};
