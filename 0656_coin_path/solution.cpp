// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

#include <climits>
#include <vector>

class Solution {
public:
    std::vector<int> cheapestJump(std::vector<int>& coins, int maxJump) {
        const int n = static_cast<int>(coins.size());
        if (coins.back() == -1) {
            return {};
        }
        const long long inf = LLONG_MAX / 4;
        std::vector<long long> cost(n, inf);
        std::vector<int> nxt(n, -1);
        cost[n - 1] = coins[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if (coins[i] == -1) {
                continue;
            }
            for (int jump = 1; jump <= maxJump; ++jump) {
                const int j = i + jump;
                if (j >= n) {
                    break;
                }
                if (cost[j] == inf) {
                    continue;
                }
                const long long candidate = coins[i] + cost[j];
                if (candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i]))) {
                    cost[i] = candidate;
                    nxt[i] = j;
                }
            }
        }
        if (cost[0] == inf) {
            return {};
        }
        std::vector<int> path = {1};
        int i = 0;
        while (i != n - 1) {
            i = nxt[i];
            path.push_back(i + 1);
        }
        return path;
    }
};
