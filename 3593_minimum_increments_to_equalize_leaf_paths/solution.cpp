// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minIncrease(int n, std::vector<std::vector<int>>& edges, std::vector<int>& cost) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        int ans = 0;
        auto dfs = [&](auto&& self, int u, int p) -> long long {
            if ((int)graph[u].size() == 1 && p != -1) return cost[u];
            std::vector<long long> childVals;
            for (int v : graph[u]) {
                if (v == p) continue;
                childVals.push_back(self(self, v, u));
            }
            if (childVals.empty()) return cost[u];
            long long mx = 0;
            for (long long c : childVals) mx = std::max(mx, c);
            for (long long c : childVals)
                if (c < mx) ans++;
            return mx + cost[u];
        };
        dfs(dfs, 0, -1);
        return ans;
    }
};
