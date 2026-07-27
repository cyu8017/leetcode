// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

#include <algorithm>
#include <cstdlib>
#include <functional>
#include <limits>
#include <vector>

class Solution {
public:
    int assignBikes(std::vector<std::vector<int>>& workers, std::vector<std::vector<int>>& bikes) {
        int m = static_cast<int>(bikes.size());
        int n = static_cast<int>(workers.size());
        std::vector<int> memo(n * (1 << m), -1);

        std::function<int(int, int)> dp = [&](int i, int mask) -> int {
            if (i == n) {
                return 0;
            }
            int key = i * (1 << m) + mask;
            if (memo[key] != -1) {
                return memo[key];
            }
            int best = std::numeric_limits<int>::max();
            int wx = workers[i][0];
            int wy = workers[i][1];
            for (int b = 0; b < m; ++b) {
                if (mask & (1 << b)) {
                    continue;
                }
                int dist = std::abs(wx - bikes[b][0]) + std::abs(wy - bikes[b][1]);
                best = std::min(best, dist + dp(i + 1, mask | (1 << b)));
            }
            return memo[key] = best;
        };

        return dp(0, 0);
    }
};
