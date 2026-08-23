// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

#include <vector>
#include <algorithm>
#include <functional>

class Solution {
public:
    std::vector<long long> placedCoins(std::vector<std::vector<int>>& edges, std::vector<int>& cost) {
        int n = (int)cost.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<long long> ans(n);
        std::function<std::vector<int>(int, int)> dfs = [&](int u, int p) -> std::vector<int> {
            std::vector<int> vals = {cost[u]};
            for (int v : g[u]) {
                if (v == p) continue;
                auto child = dfs(v, u);
                vals.insert(vals.end(), child.begin(), child.end());
            }
            std::sort(vals.begin(), vals.end());
            if ((int)vals.size() < 3) {
                ans[u] = 1;
            } else {
                int m = (int)vals.size();
                long long cand1 = (long long)vals[m - 1] * vals[m - 2] * vals[m - 3];
                long long cand2 = (long long)vals[0] * vals[1] * vals[m - 1];
                long long best = std::max(cand1, cand2);
                if (best < 0) best = 0;
                ans[u] = best;
            }
            if ((int)vals.size() <= 5) return vals;
            std::vector<int> keep;
            keep.push_back(vals[0]);
            keep.push_back(vals[1]);
            keep.push_back(vals[vals.size() - 3]);
            keep.push_back(vals[vals.size() - 2]);
            keep.push_back(vals[vals.size() - 1]);
            return keep;
        };
        dfs(0, -1);
        return ans;
    }
};
