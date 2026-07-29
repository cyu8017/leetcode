#include <algorithm>
#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    int cherryPickup(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::map<std::pair<int,int>, int> dp;
        dp[{0, n - 1}] = grid[0][0] + (n > 1 ? grid[0][n - 1] : 0);
        for (int r = 1; r < m; ++r) {
            std::map<std::pair<int,int>, int> nxt;
            for (auto& [ab, score] : dp) {
                auto [a, b] = ab;
                for (int na = a - 1; na <= a + 1; ++na)
                    for (int nb = b - 1; nb <= b + 1; ++nb)
                        if (0 <= na && na < n && 0 <= nb && nb < n) {
                            int val = score + grid[r][na] + (na != nb ? grid[r][nb] : 0);
                            auto key = std::make_pair(na, nb);
                            nxt[key] = std::max(nxt.count(key) ? nxt[key] : -1, val);
                        }
            }
            dp = std::move(nxt);
        }
        int ans = 0;
        for (auto& [_, v] : dp) ans = std::max(ans, v);
        return ans;
    }
};
