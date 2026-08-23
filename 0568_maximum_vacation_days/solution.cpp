// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxVacationDays(std::vector<std::vector<int>>& flights, std::vector<std::vector<int>>& days) {
        int cities = static_cast<int>(flights.size());
        int weeks = static_cast<int>(days[0].size());
        const int NEG = -1000000000;

        std::vector<int> dp(cities, NEG);
        dp[0] = 0;

        for (int week = 0; week < weeks; ++week) {
            std::vector<int> nxt(cities, NEG);
            for (int city = 0; city < cities; ++city) {
                if (dp[city] == NEG) {
                    continue;
                }
                for (int dest = 0; dest < cities; ++dest) {
                    if (dest == city || flights[city][dest]) {
                        nxt[dest] = std::max(nxt[dest], dp[city] + days[dest][week]);
                    }
                }
            }
            dp = std::move(nxt);
        }

        return *std::max_element(dp.begin(), dp.end());
    }
};
