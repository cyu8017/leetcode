// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxScore(int n, int k, std::vector<std::vector<int>>& stayScore, std::vector<std::vector<int>>& travelScore) {
        std::vector<int> dp(n, 0);
        for (int day = 0; day < k; day++) {
            std::vector<int> ndp(n, -(1 << 30));
            for (int dest = 0; dest < n; dest++) {
                int best = -(1 << 30);
                for (int src = 0; src < n; src++) {
                    int val = dp[src];
                    if (src == dest) val += stayScore[day][dest];
                    else val += travelScore[src][dest];
                    if (val > best) best = val;
                }
                ndp[dest] = best;
            }
            dp = ndp;
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};
