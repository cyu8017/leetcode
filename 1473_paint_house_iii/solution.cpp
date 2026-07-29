#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    int minCost(std::vector<int>& houses, std::vector<std::vector<int>>& cost, int m, int n, int target) {
        const long long inf = 1e15;
        std::map<std::pair<int,int>, long long> dp;
        dp[{0, 0}] = 0;
        for (int i = 0; i < m; ++i) {
            int painted = houses[i];
            std::map<std::pair<int,int>, long long> nxt;
            std::vector<int> colors;
            if (painted) colors.push_back(painted);
            else for (int c = 1; c <= n; ++c) colors.push_back(c);
            for (auto& [pg, value] : dp) {
                auto [prev, groups] = pg;
                for (int color : colors) {
                    int ng = groups + (color != prev);
                    if (ng <= target) {
                        long long nv = value + (painted ? 0 : cost[i][color - 1]);
                        auto key = std::make_pair(color, ng);
                        if (!nxt.count(key) || nxt[key] > nv) nxt[key] = nv;
                    }
                }
            }
            dp = std::move(nxt);
        }
        long long ans = inf;
        for (auto& [cg, v] : dp)
            if (cg.second == target) ans = std::min(ans, v);
        return ans == inf ? -1 : (int)ans;
    }
};
