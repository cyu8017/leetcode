// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

#include <algorithm>
#include <cstdint>
#include <functional>
#include <utility>
#include <vector>

class Solution {
public:
    long long maximizeSumOfWeights(std::vector<std::vector<int>>& edges, int k) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        std::function<std::pair<long long, long long>(int, int)> dfs = [&](int u, int p) -> std::pair<long long, long long> {
            long long base = 0;
            std::vector<long long> gains;
            for (auto [to, w] : g[u]) {
                if (to == p) continue;
                auto [keep, drop] = dfs(to, u);
                base += drop;
                long long gain = keep + w - drop;
                if (gain > 0) gains.push_back(gain);
            }
            std::sort(gains.begin(), gains.end(), std::greater<long long>());
            long long with = base, without = base;
            for (int i = 0; i < (int)gains.size() && i < k - 1; i++) with += gains[i];
            for (int i = 0; i < (int)gains.size() && i < k; i++) without += gains[i];
            return {with, without};
        };
        return dfs(0, -1).second;
    }
};
