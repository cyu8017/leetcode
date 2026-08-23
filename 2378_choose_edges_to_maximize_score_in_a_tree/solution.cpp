// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

#include <functional>
#include <utility>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<std::vector<int>>& edges) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (int i = 1; i < n; i++) {
            int p = edges[i - 1][0], w = edges[i - 1][1];
            g[p].push_back({i, w});
            g[i].push_back({p, w});
        }
        std::function<std::pair<long long, long long>(int, int)> dfs = [&](int u, int p) -> std::pair<long long, long long> {
            long long base = 0;
            long long bestGain = 0;
            for (auto [to, w] : g[u]) {
                if (to == p) continue;
                auto [without, with] = dfs(to, u);
                base += without;
                long long gain = with + w - without;
                if (gain > bestGain) bestGain = gain;
            }
            return {base + bestGain, base};
        };
        return dfs(0, -1).first;
    }
};
