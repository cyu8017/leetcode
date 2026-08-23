// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

#include <functional>
#include <map>
#include <vector>

class Solution {
public:
    int maximumPoints(std::vector<std::vector<int>>& edges, std::vector<int>& coins, int k) {
        int n = (int)coins.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::map<std::pair<int, int>, int> memo;
        std::function<int(int, int, int)> dfs = [&](int u, int p, int shifts) {
            if (shifts > 14) shifts = 14;
            auto key = std::make_pair(u, shifts);
            if (memo.count(key)) return memo[key];
            int c = coins[u] >> shifts;
            int opt1 = c - k, opt2 = c / 2;
            for (int v : g[u]) {
                if (v == p) continue;
                opt1 += dfs(v, u, shifts);
                opt2 += dfs(v, u, shifts + 1);
            }
            int best = opt1 > opt2 ? opt1 : opt2;
            return memo[key] = best;
        };
        return dfs(0, -1, 0);
    }
};
