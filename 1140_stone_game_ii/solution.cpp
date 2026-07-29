// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int stoneGameII(std::vector<int>& piles) {
        int n = static_cast<int>(piles.size());
        std::vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) suffix[i] = suffix[i + 1] + piles[i];
        std::vector<std::vector<int>> memo(n, std::vector<int>(n + 1, -1));
        auto dfs = [&](auto&& self, int i, int m) -> int {
            if (i >= n) return 0;
            if (i + m >= n) return suffix[i];
            if (memo[i][m] != -1) return memo[i][m];
            int bestOpp = INT_MAX;
            for (int x = 1; x <= std::min(2 * m, n - i); ++x)
                bestOpp = std::min(bestOpp, self(self, i + x, std::max(x, m)));
            return memo[i][m] = suffix[i] - bestOpp;
        };
        return dfs(dfs, 0, 1);
    }
};
