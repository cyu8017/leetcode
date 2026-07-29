// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

#include <cmath>
#include <functional>
#include <vector>

class Solution {
public:
    int countRoutes(std::vector<int>& locations, int start, int finish, int fuel) {
        constexpr int MOD = 1000000007;
        const int n = static_cast<int>(locations.size());
        std::vector<std::vector<int>> memo(n, std::vector<int>(fuel + 1, -1));

        std::function<int(int, int)> dp = [&](int city, int left) -> int {
            if (memo[city][left] != -1) {
                return memo[city][left];
            }
            long long total = (city == finish) ? 1 : 0;
            for (int nxt = 0; nxt < n; ++nxt) {
                const int cost = std::abs(locations[city] - locations[nxt]);
                if (nxt != city && cost <= left) {
                    total += dp(nxt, left - cost);
                }
            }
            return memo[city][left] = static_cast<int>(total % MOD);
        };

        return dp(start, fuel);
    }
};
